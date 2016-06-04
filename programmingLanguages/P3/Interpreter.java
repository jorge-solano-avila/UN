import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Interpreter
{
	public static void main(String[] args) throws Exception
	{
		ANTLRInputStream input = new ANTLRInputStream( System.in );

		PsiCoderLexer lexer = new PsiCoderLexer( input );

		CommonTokenStream tokens = new CommonTokenStream( lexer );

		PsiCoderParser parser = new PsiCoderParser( tokens );
		ParseTree tree = parser.psicoder();

		ParseTreeWalker walker = new ParseTreeWalker();
		walker.walk( new InterpreterPsiCoder(), tree );
		System.out.println();
	}
}