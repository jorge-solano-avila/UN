import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.border.*;

public class Analyzer
{
	public static void main( String[] args ) 
	{
		WelcomeOptiCode window = null;
		EventQueue.invokeLater( new Runnable() 
		{
			public void run() 
			{
				try 
				{
					WelcomeOptiCode window = new WelcomeOptiCode();
					window.frame.setVisible( true );
				} 
				catch( Exception e ) 
				{
					e.printStackTrace();
				}
			}
		} );
	}
}
