import java.util.*;

public class Test3
{
	public static void main( String[] args )
	{
		double b = 5.0;
		double[] array = new double[1000];
		for( int i = 0; i < 1000; i+=1 )
		{
			for( int j = 0; j < 1000; j++ )
			{
				array[j] = 6 + b;
			}
		}
	}
}