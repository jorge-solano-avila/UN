import java.util.*;

public class Test4
{
	public static void main( String[] args )
	{
		double b = 5.0;
		double[] array = new double[1000];
		for( int i = 0; i < 1000; i+=1 )
		{
			array[i] = 123;
			array[i] = 4 + b;
		}
	}
}