import org.antlr.v4.runtime.tree.*;
import java.util.*;
import javax.script.*;
import java.io.*;

public class InterpreterPsiCoder extends PsiCoderBaseListener
{
	PrintWriter writer;
	String tabs = "\t";
	String expBool = "";
	String exp = "";
	boolean isCaso = false;

	public void printDT( String str, String aux )
	{
		switch( str )
		{
			case "entero":
				writer.print( aux + "long long " );
				break;
			case "real":
				writer.print( aux + "long double " );
				break;
			case "cadena":
				writer.print( aux + "string " );
				break;
			case "caracter":
				writer.print( aux + "char " );
				break;
			case "booleano":
				writer.print( aux + "bool " );
				break;
		}
	}

	public static String strings( String str )
	{
		if( str.contains( ( CharSequence ) "\"" ) )
		{
			String aux = "string( ";
			String result = "";
			boolean flag = false, flagTwo = false;
			for( int i = 0; i < str.length(); i++ )
			{
				if( str.charAt( i ) == '"' )
				{
					if( flag )
						flagTwo = true;
					if( !flag )
						result += aux;
					flag = true;
				}
				result += str.charAt( i );
				if( flag && flagTwo )
				{
					flag = false;
					flagTwo = false;
					result += " )";
				}
			}
			return result;
		}
		return str;
	}

	@Override 
	public void enterPsicoder( PsiCoderParser.PsicoderContext ctx ) 
	{ 
		try
		{
			writer = new PrintWriter( "Interpreter.cpp", "UTF-8" );
		}
		catch( FileNotFoundException | UnsupportedEncodingException e )
		{
			System.out.println( "Error creando archivo" );
		}
		writer.println( "#include<iostream>" );
		writer.println( "#include<string>" );
		writer.println( "using namespace std;\n" );
	}

	@Override 
	public void exitPsicoder( PsiCoderParser.PsicoderContext ctx ) 
	{ 
		writer.close();
	}
	
	@Override 
	public void enterEstructura( PsiCoderParser.EstructuraContext ctx ) 
	{	
		writer.println( "struct " + ctx.ID().getText() );
		writer.println( "{" );
	}

	@Override 
	public void exitEstructuraAux1( PsiCoderParser.EstructuraAux1Context ctx ) 
	{
		writer.println( "};" );
	}

	@Override 
	public void enterEstructuraAux( PsiCoderParser.EstructuraAuxContext ctx ) 
	{
		if( ctx.ID() != null )
		{
			writer.print( "\t" + ctx.ID().getText() + " " );
		}
		else if( ctx.dt() != null )
		{
			printDT( ctx.dt().getText(), "\t" );
		}
	}

	@Override 
	public void exitGlobalAux1( PsiCoderParser.GlobalAux1Context ctx ) 
	{
		writer.println( ";" );
	}

	@Override 
	public void enterGlobalAux( PsiCoderParser.GlobalAuxContext ctx ) 
	{ 
		if( ctx.ID() != null )
		{
			writer.print( ctx.ID().getText() );	
		}
	}

	@Override 
	public void enterGlobalAuxAux( PsiCoderParser.GlobalAuxAuxContext ctx ) 
	{ 
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( ", " );
			}
		}
	}
	
	@Override 
	public void enterFuncion( PsiCoderParser.FuncionContext ctx ) 
	{
		if( ctx.tipoFuncionID != null )
		{
			writer.print( ctx.tipoFuncionID.getText() + " " );
		}
		else if( ctx.tipoFuncion != null )
		{
			printDT( ctx.tipoFuncion.getText(), "" );
		}
		writer.print( ctx.idFuncion.getText() + "( " );
	}

	@Override 
	public void exitParametro1( PsiCoderParser.Parametro1Context ctx ) 
	{ 
		writer.println( " )\n{" );
	}

	@Override 
	public void enterParametroAux( PsiCoderParser.ParametroAuxContext ctx ) 
	{
		if( ctx.tipoParametro != null )
		{
			writer.print( ctx.tipoParametro.getText() + " " );
		}
		else
		{
			printDT( ctx.dt().getText(), "" );
		}
		writer.print( ctx.idParametro.getText() );
	}

	@Override 
	public void enterParametroAuxAux( PsiCoderParser.ParametroAuxAuxContext ctx ) 
	{
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( ", " );
			}
		}
	}
	
	@Override 
	public void enterRetornar( PsiCoderParser.RetornarContext ctx ) 
	{ 
		writer.print( tabs + "return " );
		if( ctx.expresion() != null )
		{
			writer.print( strings( ctx.expresion().getText() ) );
		}
		else if( ctx.expBool() != null )
		{
			String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
			aux = aux.replaceAll( "verdadero", "true" );
			writer.print( aux );
		}
		writer.println( ";\n}" );
	}

	@Override 
	public void enterVariableG( PsiCoderParser.VariableGContext ctx ) 
	{ 
		if( ctx.dt() != null )
		{
			printDT( ctx.dt().getText(), "" );
		}
		else if( ctx.ID() != null )
		{
			writer.print( ctx.ID().getText() + " " );
		}
	}

	@Override 
	public void exitComaAsignacion1( PsiCoderParser.ComaAsignacion1Context ctx ) 
	{
		writer.println( ";" );
	}

	@Override 
	public void exitComaAsignacion2( PsiCoderParser.ComaAsignacion2Context ctx ) 
	{
		writer.println( ";" );
	}

	@Override 
	public void enterComaAsignacion( PsiCoderParser.ComaAsignacionContext ctx ) 
	{ 
		writer.print( ctx.ID().getText() );
	}

	@Override 
	public void enterComaAsignacionAux( PsiCoderParser.ComaAsignacionAuxContext ctx ) 
	{ 
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == '=' )
			{
				writer.print( " = " );
				if( ctx.expresion() != null )
				{
					writer.print( strings( ctx.expresion().getText() ) );
				}
				else if( ctx.expBool() != null )
				{
					String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
					aux = aux.replaceAll( "verdadero", "true" );
					writer.print( aux );
				}
			}
			else if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( ", " );
			}
		}
	}

	@Override 
	public void enterComaAsignacionAuxAux( PsiCoderParser.ComaAsignacionAuxAuxContext ctx ) 
	{
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( ", " );
			}
		}
	}

	@Override 
	public void enterIdContenido( PsiCoderParser.IdContenidoContext ctx ) 
	{
		if( ctx.ID() != null )
		{ 
			writer.print( tabs + ctx.ID().getText() );
		}
	}

	@Override 
	public void enterIdAux( PsiCoderParser.IdAuxContext ctx ) 
	{
		if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == '=' )
		{
			writer.print( " = " );
			if( ctx.expID != null )
			{
				writer.print( strings( ctx.expID.getText() ) );
			}
			else if( ctx.expBID != null )
			{
				String aux = ctx.expBID.getText().replaceAll( "falso", "false" );
				aux = aux.replaceAll( "verdadero", "true" );
				writer.print( aux );
			}
			writer.println( ";" );
		}
		else if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == '(' )
		{
			writer.print( "( " );
			if( ctx.expID2 != null )
			{
				expBool = strings( ctx.expID2.getText() );
			}
			else if( ctx.expBID2 != null )
			{
				exp = ctx.expBID2.getText();
			}
		}
		else if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == '.' )
		{
			writer.print( "." );
			if( ctx.expID1 != null )
			{
				expBool = strings( ctx.expID1.getText() );
			}
			else if( ctx.expBID1 != null )
			{
				exp = ctx.expBID1.getText();
			}
		}
	}

	@Override 
	public void enterComaExpresion1( PsiCoderParser.ComaExpresion1Context ctx ) 
	{
		if( !exp.equals( "" ) )
		{
			writer.print( exp );
			exp = "";
		}
		else if( !expBool.equals( "" ) )
		{
			writer.print( expBool );
			expBool = "";
		}
	}

	@Override 
	public void exitComaExpresion1( PsiCoderParser.ComaExpresion1Context ctx ) 
	{ 
		writer.println( " );" );
	}

	@Override 
	public void enterComaExpresion( PsiCoderParser.ComaExpresionContext ctx ) 
	{
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( ", " );
				if( ctx.expresion() != null )
				{
					writer.print( strings( ctx.expresion().getText() ) );
				}
				else if( ctx.expBool() != null )
				{
					String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
					aux = aux.replaceAll( "verdadero", "true" );
					writer.print( aux );
				}
			}
		}
	}

	@Override 
	public void exitEstructuraPunto1( PsiCoderParser.EstructuraPunto1Context ctx ) 
	{
		writer.print( " = " );
		if( !exp.equals( "" ) )
		{
			writer.println( exp + ";" );
			exp = "";
		}
		else if( !expBool.equals( "" ) )
		{
			writer.println( expBool + ";" );
			expBool = "";
		}
	}

	@Override 
	public void enterEstructuraPunto( PsiCoderParser.EstructuraPuntoContext ctx ) 
	{
		writer.print( ctx.ID().getText() );
	}

	@Override 
	public void enterEstructuraPuntoAux( PsiCoderParser.EstructuraPuntoAuxContext ctx ) 
	{
		if( ctx != null && ctx.getText().length() > 0 )
		{
			writer.print( "." );
		}
	}

	@Override 
	public void enterVariable( PsiCoderParser.VariableContext ctx ) 
	{ 
		if( ctx.dt() != null )
		{
			printDT( ctx.dt().getText(), tabs );
		}
		else if( ctx.ID() != null )
		{
			writer.print( tabs + ctx.ID().getText() + " " );
		}
	}

	@Override 
	public void enterLeer( PsiCoderParser.LeerContext ctx ) 
	{
		writer.println( tabs + "cin >> " + ctx.ID().getText() + ";" );
	}

	@Override 
	public void enterImprimir( PsiCoderParser.ImprimirContext ctx ) 
	{
		writer.print( tabs + "cout << " );
		if( ctx.expresion() != null )
		{
			writer.print( strings( ctx.expresion().getText() ) );
		}
		else if( ctx.expBool() != null )
		{
			String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
			aux = aux.replaceAll( "verdadero", "true" );
			writer.print( aux );
		}
	}

	@Override 
	public void exitComaImpresion1( PsiCoderParser.ComaImpresion1Context ctx ) 
	{ 
		writer.println( " << endl;" );
	}

	@Override 
	public void enterComaImpresion( PsiCoderParser.ComaImpresionContext ctx ) 
	{ 
		if( ctx != null )
		{
			if( ctx.getText().length() > 0 && ctx.getText().charAt( 0 ) == ',' )
			{
				writer.print( " << " );
				if( ctx.expresion() != null )
				{
					String aux = ctx.expresion().getText().replaceAll( "falso", "false" );
					aux = aux.replaceAll( "verdadero", "true" );
					writer.print( strings( aux ) );
				}
				else if( ctx.expBool() != null )
				{
					String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
					aux = aux.replaceAll( "verdadero", "true" );
					writer.print( aux );
				}
			}
		}
	}
	
	@Override 
	public void enterSi( PsiCoderParser.SiContext ctx ) 
	{
		String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
		aux = aux.replaceAll( "verdadero", "true" );
		writer.println( tabs + "if( " + aux + " )\n" + tabs + "{" );
		tabs += "\t"; 
	}

	@Override 
	public void exitSiNo1( PsiCoderParser.SiNo1Context ctx ) 
	{
		tabs = tabs.substring( 0, tabs.length() - 1 );
		writer.println( tabs + "}" );
	}

	@Override 
	public void enterSiNo( PsiCoderParser.SiNoContext ctx ) 
	{
		if( ctx != null && ctx.getText().length() > 0 )
		{
			tabs = tabs.substring( 0, tabs.length() - 1 );
			writer.println( tabs + "}" );
			writer.println( tabs + "else\n" + tabs + "{" );
			tabs += "\t"; 
		}
	}
	
	@Override 
	public void enterMientras( PsiCoderParser.MientrasContext ctx ) 
	{ 
		String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
		aux = aux.replaceAll( "verdadero", "true" );
		writer.println( tabs + "while( " + aux + " )\n" + tabs + "{" );
		tabs += "\t";
	}

	@Override 
	public void exitPrincipal1( PsiCoderParser.Principal1Context ctx ) 
	{
		tabs = tabs.substring( 0, tabs.length() - 1 );
		writer.println( tabs + "}" );
	}
	
	@Override 
	public void enterHacer( PsiCoderParser.HacerContext ctx ) 
	{
		writer.println( tabs + "do\n" + tabs + "{" );
		String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
		aux = aux.replaceAll( "verdadero", "true" );
		expBool = aux;
		tabs += "\t";
	}
	
	@Override 
	public void exitPrincipalHacer( PsiCoderParser.PrincipalHacerContext ctx ) 
	{
		tabs = tabs.substring( 0, tabs.length() - 1 );
		writer.println( tabs + "}\n" + tabs + "while( " + expBool + " );" );
		expBool = "";

	}
	
	@Override 
	public void enterPara( PsiCoderParser.ParaContext ctx ) 
	{
		writer.print( tabs + "for( " );
		if( ctx.tipoInicializacion != null )
		{
			writer.print( "int " );
		}
		String aux = ctx.expBool().getText().replaceAll( "falso", "false" );
		aux = aux.replaceAll( "verdadero", "true" );
		writer.println( ctx.idPara.getText() + " = " + ctx.expInicializacion.getText() 
			+ "; " + aux + "; " + ctx.idPara.getText() + " += " 
			+ ctx.expIncremento.getText() + " )\n" + tabs + "{" );
		tabs += "\t";
	}
	
	@Override 
	public void exitPrincipalPara( PsiCoderParser.PrincipalParaContext ctx ) 
	{
		tabs = tabs.substring( 0, tabs.length() - 1 );
		writer.println( tabs + "}" );
	}
	
	@Override 
	public void enterSeleccionar( PsiCoderParser.SeleccionarContext ctx ) 
	{ 
		writer.println( tabs + "switch( " + ctx.ID().getText() + " )\n" + tabs + "{" );
		tabs += "\t";
	}

	@Override 
	public void enterSeleccionarAux( PsiCoderParser.SeleccionarAuxContext ctx ) 
	{
		String str = ctx.getText();
		if( str.length() > 0 && str.charAt( 0 ) == 'd' )
		{
			if( isCaso )
				tabs = tabs.substring( 0, tabs.length() - 1 );
			writer.println( tabs + "default:" );
			tabs += "\t";
		}
		if( str.length() > 0 && str.charAt( 0 ) == 'c' )
		{
			if( isCaso )
				tabs = tabs.substring( 0, tabs.length() - 1 );
			isCaso = true;
			writer.println( tabs + "case " + ctx.INT().getText() + ":" );
			tabs += "\t";
		}
	}

	@Override 
	public void exitSeleccionarAux1( PsiCoderParser.SeleccionarAux1Context ctx ) 
	{
		tabs = tabs.substring( 0, tabs.length() - 2 );
		writer.println( tabs + "}" );
		isCaso = false;
	}
	
	@Override 
	public void enterRomper( PsiCoderParser.RomperContext ctx ) 
	{ 
		writer.println( tabs + "break;" );
	}

	@Override 
	public void visitTerminal( TerminalNode node ) 
	{
		if( node != null && node.getText().equals( "funcion_principal" ) )
		{
			writer.println( "int main()" );
			writer.println( "{" );
		}
		if( node != null && node.getText().equals( "fin_principal" ) )
		{
			writer.println( "}" );
		}
	}
}