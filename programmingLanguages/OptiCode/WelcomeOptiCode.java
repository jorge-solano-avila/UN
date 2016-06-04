import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class WelcomeOptiCode extends JFrame
{
	private static final long serialVersionUID = 1L;
	JFrame frame;
	private String path = new String();

	public WelcomeOptiCode() 
	{
		initialize();
	}

	private void initialize() 
	{
		frame = new JFrame( "OptiCode - Lenguajes de programaci\u00F3n" );
		frame.setResizable( false );
		frame.getContentPane().setBackground( SystemColor.inactiveCaptionBorder );
		
		JButton btnSi = new JButton( "Go!" );
		btnSi.addActionListener( new ActionListener() 
		{
			public void actionPerformed( ActionEvent e ) 
			{
				frame.dispose();
				ChooseFile opt = new ChooseFile();
				path = opt.getPath();
				opt.setEnabled( true );
				opt.setVisible( true );
			}
		});
		btnSi.setFont(new Font("Tahoma", Font.PLAIN, 16));
		btnSi.setBounds(173, 202, 108, 46);
		frame.getContentPane().setLayout(null);
		frame.getContentPane().add(btnSi);
		
		JLabel lblBienvenidoAOpticode = new JLabel( "Bienvenido a OptiCode:" );
		lblBienvenidoAOpticode.setHorizontalAlignment(SwingConstants.CENTER);
		lblBienvenidoAOpticode.setForeground( Color.RED );
		lblBienvenidoAOpticode.setFont( new Font( "Ravie", Font.PLAIN, 20 ) );
		lblBienvenidoAOpticode.setBounds( 70, 12, 313, 65 );
		frame.getContentPane().add( lblBienvenidoAOpticode );
		
		JLabel lblRecomendacionesDeUso = new JLabel("Recomendaciones de uso:");
		lblRecomendacionesDeUso.setFont(new Font("Dialog", Font.BOLD, 16));
		lblRecomendacionesDeUso.setHorizontalAlignment(SwingConstants.CENTER);
		lblRecomendacionesDeUso.setBounds(80, 89, 303, 28);
		frame.getContentPane().add(lblRecomendacionesDeUso);
		
		JLabel lblElCdigo = new JLabel("1) El código debe compilar.");
		lblElCdigo.setBounds(141, 123, 232, 15);
		frame.getContentPane().add(lblElCdigo);
		frame.setBackground( SystemColor.controlHighlight );
		frame.setBounds( 100, 100, 450, 300 );
		frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
	}
	
	public String getPath()
	{
		return path;
	}
}
