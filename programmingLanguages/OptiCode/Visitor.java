import java.util.*;

public class Visitor extends Java8BaseVisitor<String>
{
	String type = new String();
	String tabs = new String();
	String codeDead = new String();
	String identifierMethod = new String();
	int countVariables = 1;
	boolean entryFor = false; 
	boolean printMethod = false;
	boolean entryLoop = false;
	boolean entryMethod = false;
	boolean print = true;
	boolean analysis = false;
	boolean replaceVariable = false;
	boolean eliminateCodeDead = false;
	// Expressions completes
	List<Value> expressions = new ArrayList<>();
	List<String> variables = new ArrayList<>();
	List<String> replace = new ArrayList<>();
	Map<String, String> types = new HashMap<>();

	public void printLoop()
	{
		int count = countVariables;
		if( expressions.size() != 0 )
		{
			for( int i = 0; i < expressions.size(); ++i )
			{
				Value aux = expressions.get( i );
				replace.add( aux.getVariable() );
				String variable = aux.getVariable();
				int temp = 0, temp3 = 0;
				if( variable.contains( "[" ) )
				{
					for( int j = 0; j < variable.length(); ++j )
						if( variable.charAt( j ) == '[' )
						{
							temp = j;
							break;
						}
					String temp2 = types.get( variable.substring( 0, temp ) );
					if( temp2.contains( "[" ) )
					{
						for( int k = 0; k < temp2.length(); ++k )
							if( temp2.charAt( k ) == '[' )
							{
								temp3 = k;
								break;
							}
						System.out.println( tabs + temp2.substring( 0, temp3 ) + " newVariable" + countVariables++ + " = " 
							+ aux.getExpression() + ";" );
					}
					else
						System.out.println( tabs + types.get( variable.substring( 0, temp ) ) + " newVariable" + countVariables++ + " = " 
							+ aux.getExpression() + ";" );
				}
				else
					System.out.println( tabs + types.get( aux.getVariable() ) + " newVariable" + countVariables++ + " = " 
						+ aux.getExpression() + ";" );
			}
		}
	}

	public static ArrayList<String> literals( String expression )
	{
		return new ArrayList<>( Arrays.asList( expression.split( "\\s*[^a-zA-Z]+\\s*" ) ) );
	}

	@Override
	public String visitPackageDeclaration( Java8Parser.PackageDeclarationContext ctx ) 
	{
		String aux = ctx.getText();
		if( aux.contains( "package" ) )
			aux = aux.replaceAll( "package", "package " );
		System.out.println( aux );
		return null;
	}

	@Override
	public String visitImportDeclaration( Java8Parser.ImportDeclarationContext ctx ) 
	{
		String aux = ctx.getText();
		if( aux.contains( "import" ) )
			aux = aux.replaceAll( "import", "import " );
		System.out.println( aux );
		return null;
	}

	@Override
	public String visitNormalClassDeclaration( Java8Parser.NormalClassDeclarationContext ctx ) 
	{
		List<Java8Parser.ClassModifierContext> list = ctx.classModifier();
		for( Java8Parser.ClassModifierContext context : list )
			visit( context );
		System.out.println( "class " + ctx.Identifier() );
		visit( ctx.classBody() );
		return null;
	}

	@Override
	public String visitClassBody( Java8Parser.ClassBodyContext ctx ) 
	{
		List<Java8Parser.ClassBodyDeclarationContext> list = ctx.classBodyDeclaration();
		System.out.println( "{" );
		tabs += "\t";
		for( Java8Parser.ClassBodyDeclarationContext context : list )
			visit( context );
		System.out.println( "}" );
		return null;
	}

	@Override
	public String visitClassModifier( Java8Parser.ClassModifierContext ctx ) 
	{
		System.out.print( ctx.getText() + " " );
		visitChildren( ctx );
		return null;
	}

	@Override
	public String visitFieldDeclaration( Java8Parser.FieldDeclarationContext ctx ) 
	{
		type = ctx.unannType().getText();
		System.out.print( tabs + ctx.unannType().getText() + " " );
		visit( ctx.variableDeclaratorList() );
		System.out.println( ";" );
		return null;
	}

	@Override
	public String visitMethodDeclaration( Java8Parser.MethodDeclarationContext ctx ) 
	{
		List<Java8Parser.MethodModifierContext> list = ctx.methodModifier();
		if( printMethod )
			System.out.println();
		System.out.print( tabs );
		printMethod = true;
		for( Java8Parser.MethodModifierContext context : list )
			visit( context );
		visit( ctx.methodHeader() );
		visit( ctx.methodBody() );
		return null;
	}

	@Override
	public String visitMethodModifier( Java8Parser.MethodModifierContext ctx ) 
	{
		System.out.print( ctx.getText() + " " );
		visitChildren( ctx );
		return null;
	}

	@Override 
	public String visitMethodBody( Java8Parser.MethodBodyContext ctx ) 
	{
		if( identifierMethod.equals( "main" ) )
		{
			visitChildren( ctx );
		} 
		else
		{
			entryMethod = true; 
			analysis = true;
			visitChildren( ctx );
			analysis = false;
			if( !codeDead.contains( "return" ) )
				eliminateCodeDead = true;
			visitChildren( ctx );
			codeDead = new String();
			entryMethod = false;
			eliminateCodeDead = false;
		}
		return null; 
	}

	@Override
	public String visitResult( Java8Parser.ResultContext ctx ) 
	{
		System.out.print( ctx.getText() + " " );
		return null;
	}

	@Override
	public String visitMethodDeclarator( Java8Parser.MethodDeclaratorContext ctx ) 
	{
		System.out.print( ctx.Identifier() + "( " );
		identifierMethod = ctx.Identifier().getText();
		visitChildren( ctx );
		return null;
	}

	@Override
	public String visitFormalParameterList( Java8Parser.FormalParameterListContext ctx ) 
	{
		if( ctx.getChildCount() == 3 )
			visit( ctx.formalParameters() );
		visit( ctx.lastFormalParameter() );
		return null;
	}

	@Override
	public String visitFormalParameters( Java8Parser.FormalParametersContext ctx ) 
	{
		List<Java8Parser.FormalParameterContext> list = ctx.formalParameter();
		for( Java8Parser.FormalParameterContext context : list )
		{
			visit( context );
			System.out.print( ", " );
		}
		return null;
	}

	@Override
	public String visitLastFormalParameter( Java8Parser.LastFormalParameterContext ctx ) 
	{
		visit( ctx.formalParameter() );
		System.out.println( " )" );
		return null;
	}

	@Override
	public String visitFormalParameter( Java8Parser.FormalParameterContext ctx ) 
	{
		types.put( ctx.variableDeclaratorId().getText(), ctx.unannType().getText() );
		System.out.print( ctx.unannType().getText() + " " 
			+ ctx.variableDeclaratorId().getText() );
		return null;
	}

	@Override
	public String visitBlock( Java8Parser.BlockContext ctx ) 
	{
		if( !analysis )
		{
			if( !entryLoop )
				System.out.println( tabs + "{" );
			tabs += "\t";
			visit( ctx.blockStatements() );
			tabs = tabs.substring( 0, tabs.length() - 1 );
			System.out.println( tabs + "}" );
		}
		else
			visit( ctx.blockStatements() );
		return null;
	}

	@Override
	public String visitBlockStatement( Java8Parser.BlockStatementContext ctx ) 
	{
		if( analysis && entryMethod )
		{
			codeDead = ctx.getText();
			return null;
		}
		else if( entryMethod && eliminateCodeDead && ctx.getText().equals( codeDead ) )
			return null;
		else
			visitChildren( ctx );
		return null;
	}

	@Override
	public String visitLocalVariableDeclaration( Java8Parser.LocalVariableDeclarationContext ctx ) 
	{
		if( entryFor )
		{
			type = ctx.unannType().getText();
			System.out.print( ctx.unannType().getText() + " " );
			visit( ctx.variableDeclaratorList() );
		}
		else
		{
			type = ctx.unannType().getText();
			System.out.print( tabs + ctx.unannType().getText() + " " );
			visit( ctx.variableDeclaratorList() );
			System.out.println( ";" );
		}
		return null;
	}

	@Override
	public String visitVariableDeclaratorList( Java8Parser.VariableDeclaratorListContext ctx ) 
	{
		if( ctx.getChildCount() >= 3 )
			for( int i = 0; i < ctx.getChildCount(); ++i )
				if( i % 2 == 0 )
					visit( ctx.getChild( i ) );
				else
					System.out.print( ", " );
		else
			visit( ctx.variableDeclarator( 0 ) );
		return null;
	}

	@Override
	public String visitVariableDeclarator( Java8Parser.VariableDeclaratorContext ctx ) 
	{
		types.put( ctx.variableDeclaratorId().getText(), type );
		System.out.print( ctx.variableDeclaratorId().getText() );
		if( ctx.getChildCount() >= 3 )
		{
			String aux = ctx.variableInitializer().getText();
			if( aux.contains( "new" ) )
				aux = aux.replaceAll( "new", "new " );
			System.out.print( " = "	+ aux );
		}
		return null;
	}

	@Override
	public String visitWhileStatement( Java8Parser.WhileStatementContext ctx ) 
	{
		if( !entryLoop )
		{
			entryLoop = true;
			analysis = true;
			visit( ctx.statement() );
			int count = countVariables;
			printLoop();
			analysis = false;
			System.out.println( tabs + "while( " + ctx.expression().getText() + " )" );
			System.out.println( tabs + "{" );
			if( expressions.size() != 0 )
			{
				for( int i = 0; i < expressions.size(); ++i )
				{
					Value aux = expressions.get( i );
					System.out.println( tabs + "\t" + aux.getVariable() + " " + aux.getAssign() 
						+ " newVariable" + count++ + ";" );
				}
			}
			expressions = new ArrayList<Value>();
			variables = new ArrayList<String>();
			visit( ctx.statement() );
			entryLoop = false;
		}
		else if( !analysis )
		{
			analysis = true;
			visit( ctx.statement() );
			int count = countVariables;
			printLoop();
			analysis = false;
			System.out.println( tabs + "while( " + ctx.expression().getText() + " )" );
			if( expressions.size() != 0 )
			{
				for( int i = 0; i < expressions.size(); ++i )
				{
					Value aux = expressions.get( i );
					System.out.println( tabs + "\t" + aux.getVariable() + " " + aux.getAssign() 
						+ " newVariable" + count++ + ";" );
				}
			}
			expressions = new ArrayList<Value>();
			visit( ctx.statement() );
		}
		return null;
	}

	@Override
	public String visitIfThenStatement( Java8Parser.IfThenStatementContext ctx ) 
	{
		System.out.println( tabs + "if( " + ctx.expression().getText() + " )" );
		visit( ctx.statement() );
		return null;
	}

	@Override
	public String visitBasicForStatement( Java8Parser.BasicForStatementContext ctx ) 
	{
		if( !entryLoop )
		{
			entryLoop = true;
			analysis = true;
			visit( ctx.statement() );
			int count = countVariables;
			printLoop();
			analysis = false;
			entryFor = true;
			System.out.print( tabs + "for( " );
			visit( ctx.forInit() );
			System.out.print( "; " + ctx.expression().getText() + "; " );
			visit( ctx.forUpdate() );
			System.out.println( " )" );
			System.out.println( tabs + "{" );
			if( expressions.size() != 0 )
			{
				for( int i = 0; i < expressions.size(); ++i )
				{
					Value aux = expressions.get( i );
					System.out.println( tabs + "\t" + aux.getVariable() + " " + aux.getAssign() 
						+ " newVariable" + count++ + ";" );
				}
			}
			expressions = new ArrayList<Value>();
			variables = new ArrayList<String>();
			entryFor = false;
			visit( ctx.statement() );
			entryLoop = false;
		}
		else if( !analysis )
		{
			analysis = true;
			visit( ctx.statement() );
			int count = countVariables;
			printLoop();
			analysis = false;
			entryFor = true;
			System.out.print( tabs + "for( " );
			visit( ctx.forInit() );
			System.out.print( "; " + ctx.expression().getText() + "; " );
			visit( ctx.forUpdate() );
			System.out.println( " )" );
			System.out.println( tabs + "{" );
			if( expressions.size() != 0 )
			{
				for( int i = 0; i < expressions.size(); ++i )
				{
					Value aux = expressions.get( i );
					System.out.println( tabs + "\t" + aux.getVariable() + " " + aux.getAssign() 
						+ " newVariable" + count++ + ";" );
				}
			}
			expressions = new ArrayList<Value>();
			entryFor = false;
			visit( ctx.statement() );
		}
		return null;
	}

	@Override
	public String visitAssignment( Java8Parser.AssignmentContext ctx ) 
	{
		if( entryFor && !analysis )
		{
			System.out.print( ctx.leftHandSide().getText() + " " 
				+ ctx.assignmentOperator().getText() + " " + ctx.expression().getText() );
		}
		else if( !analysis )
		{
			if( !replace.contains( ctx.leftHandSide().getText() ) )
			{
				System.out.print( tabs + ctx.leftHandSide().getText() + " " 
					+ ctx.assignmentOperator().getText() + " " + ctx.expression().getText() );
				
			}
			else
				replaceVariable = true;
		}
		else
		{
			variables.add( ctx.leftHandSide().getText() );
			String expression = ctx.expression().getText();
			ArrayList<String> aux = literals( expression );
			for( int i = 1; i < aux.size(); ++i )
				if( !variables.contains( aux.get( i ) ) )
					expressions.add( new Value( ctx.leftHandSide().getText(), 
						ctx.assignmentOperator().getText(), ctx.expression().getText() ) );
		}
		return null;
	}

	@Override
	public String visitEnhancedForStatement( Java8Parser.EnhancedForStatementContext ctx ) 
	{
		types.put( ctx.variableDeclaratorId().getText(), ctx.variableDeclaratorId().getText() );
		System.out.println( tabs + "for( " + ctx.unannType().getText() + " " 
			+ ctx.variableDeclaratorId().getText() + " : " + ctx.expression().getText() + " )" );
		visit( ctx.statement() );
		return null;
	}

	@Override
	public String visitReturnStatement( Java8Parser.ReturnStatementContext ctx ) 
	{
		String aux = ctx.expression().getText();
		if( aux.contains( "new" ) )
			aux = aux.replaceAll( "new", "new " );
		System.out.println( tabs + "return " + aux + ";" );
		return null;
	}

	@Override
	public String visitMethodInvocation( Java8Parser.MethodInvocationContext ctx ) 
	{
		System.out.print( tabs + ctx.typeName().getText() + "." + ctx.Identifier() 
			+ "( " );
		visit( ctx.argumentList() );
		System.out.print( " )" );
		return null;
	}

	@Override
	public String visitArgumentList( Java8Parser.ArgumentListContext ctx ) 
	{
		if( ctx.getChildCount() >= 3 )
			for( int i = 0; i < ctx.getChildCount(); ++i )
				if( i % 2 == 0 )
				{
					String aux = ctx.getChild( i ).getText();
					if( aux.contains( "new" ) )
						aux = aux.replaceAll( "new", "new " );
					System.out.print( aux );
				}
				else
					System.out.print( ", " );
		else
		{
			String aux = ctx.expression( 0 ).getText();
			if( aux.contains( "new" ) )
				aux = aux.replaceAll( "new", "new " );
			System.out.print( aux );
		}
		return null;
	}

	@Override
	public String visitExpressionStatement( Java8Parser.ExpressionStatementContext ctx ) 
	{
		visit( ctx.statementExpression() );
		if( !replaceVariable && !analysis )
			System.out.println( ";" );
		else
			replaceVariable = false;
		return null;
	}

	@Override
	public String visitPreDecrementExpression( Java8Parser.PreDecrementExpressionContext ctx ) 
	{
		if( entryFor )
			System.out.print( "--" + ctx.unaryExpression().getText() );
		else
			System.out.print( tabs + "--" + ctx.unaryExpression().getText() );
		return null;
	}

	@Override
	public String visitPreIncrementExpression( Java8Parser.PreIncrementExpressionContext ctx ) 
	{
		if( entryFor )
			System.out.print( "++" + ctx.unaryExpression().getText() );
		else
			System.out.print( tabs + "++" + ctx.unaryExpression().getText() );
		return null;
	}

	@Override
	public String visitPostDecrementExpression( Java8Parser.PostDecrementExpressionContext ctx ) 
	{
		if( entryFor )
			System.out.print( ctx.postfixExpression().getText() + "--" );
		else
			System.out.print( tabs + ctx.postfixExpression().getText() + "--" );
		return null;
	}

	@Override
	public String visitPostIncrementExpression( Java8Parser.PostIncrementExpressionContext ctx ) 
	{
		if( entryFor )
			System.out.print( ctx.postfixExpression().getText() + "++" );
		else
			System.out.print( tabs + ctx.postfixExpression().getText() + "++" );
		return null;
	}
}

class Value
{
	private String variable = new String();
	private String assign = new String();
	private String expression = new String();

	public Value( String variable, String assign, String expression )
	{
		this.variable = variable;
		this.assign = assign;
		this.expression = expression;
	}

	public void setVariable( String variable )
	{
		this.variable = variable;
	}

	public void setAssign( String assign )
	{
		this.assign = assign;
	}

	public void setExpression( String expression )
	{
		this.expression = expression;
	}

	public String getVariable()
	{
		return variable;
	}

	public String getAssign()
	{
		return assign;
	}

	public String getExpression()
	{
		return expression;
	}
}