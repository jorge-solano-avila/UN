import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import javax.swing.border.*;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class ChooseFile extends JFrame 
{
	private static final long serialVersionUID = 1L;
	
	private JPanel contentPane;
	private JTextField textField;
	FileManager tc = new FileManager();
    Boolean isnew = true;
    private String path = new String();

	public ChooseFile() 
	{
		setTitle("OptiCode - Lenguajes de programaci\u00F3n");
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 548, 404);
		contentPane = new JPanel();
		contentPane.setBackground(SystemColor.inactiveCaptionBorder);
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblOpticode = new JLabel("OptiCode");
		lblOpticode.setHorizontalAlignment(SwingConstants.CENTER);
		lblOpticode.setForeground(Color.RED);
		lblOpticode.setFont(new Font("Dialog", Font.PLAIN, 30));
		lblOpticode.setBounds(175, 12, 210, 59);
		contentPane.add(lblOpticode);
		
		JLabel lblPorFavorSeleccione = new JLabel("Por favor seleccione el archivo que desea optimizar...");
		lblPorFavorSeleccione.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblPorFavorSeleccione.setBounds(31, 94, 503, 25);
		contentPane.add(lblPorFavorSeleccione);
		
		textField = new JTextField();
		textField.setEditable(false);
		textField.setBounds(247, 171, 271, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		JButton button = new JButton("Optimizar");
		button.setEnabled(false);
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Result tf = new Result();
				tf.setEnabled(true);
				tf.setVisible(true);
				ANTLRInputStream input = null;
				try 
				{
					input = new ANTLRFileStream( path );
				} 
				catch( IOException error ) 
				{
					error.printStackTrace();
				}

		        Java8Lexer lexer = new Java8Lexer( input );

		        CommonTokenStream tokens = new CommonTokenStream( lexer );

		        Java8Parser parser = new Java8Parser( tokens );
		        ParseTree tree = parser.compilationUnit();
		        Visitor visitor = new Visitor();
		        visitor.visit( tree );
			}
		});
		button.setFont(new Font("Tahoma", Font.PLAIN, 16));
		button.setBounds(194, 266, 191, 59);
		contentPane.add(button);
		
		JButton btnSeleccionarArchivo = new JButton("Seleccionar archivo");
		btnSeleccionarArchivo.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser fc=new JFileChooser();
				
				int seleccion=fc.showOpenDialog(contentPane);
				if(seleccion==JFileChooser.APPROVE_OPTION){
					File fichero=fc.getSelectedFile();
					textField.setText(fichero.getAbsolutePath());
					path = fichero.getAbsolutePath();
					button.setEnabled(true);
				}
			}
		});
		btnSeleccionarArchivo.setFont(new Font("Tahoma", Font.PLAIN, 16));
		btnSeleccionarArchivo.setBounds(46, 150, 191, 59);
		contentPane.add(btnSeleccionarArchivo);		
	}
	
	public String getPath()
	{
		return path;
	}
}
