import javax.swing.*;

public class Result extends JFrame {

	private static final long serialVersionUID = 1L;

	public Result() {
        initComponents();
        this.setTitle("OptiCode");
    }
    
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jScrollPane1 = new javax.swing.JScrollPane();
        TEXTO = new javax.swing.JTextArea();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        smSave1 = new javax.swing.JMenuItem();
        jMenu2 = new javax.swing.JMenu();
        smAcerca = new javax.swing.JMenuItem();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));

        TEXTO.setColumns(20);
        TEXTO.setRows(5);
        TEXTO.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                TEXTOKeyReleased(evt);
            }
        });
        jScrollPane1.setViewportView(TEXTO);

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 570, Short.MAX_VALUE)
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 461, Short.MAX_VALUE)
        );

        jMenu1.setText("Archivo");

        smSave1.setText("Guardar");
        smSave1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                smSave1ActionPerformed(evt);
            }
        });
        jMenu1.add(smSave1);

        jMenuBar1.add(jMenu1);

        jMenu2.setText("Ayuda");

        smAcerca.setText("Acerca de...");
        smAcerca.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                smAcercaActionPerformed(evt);
            }
        });
        jMenu2.add(smAcerca);

        jMenuBar1.add(jMenu2);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        pack();
    }//                         

    private void smSave1ActionPerformed(java.awt.event.ActionEvent evt) {                                        
        if (isnew) {
           isnew = tc.Dialog("Save As", TEXTO);
           this.setTitle(title + tc.ruta);
        }
        else
        {                 
            isnew=tc.Dialog("Save", TEXTO);   
            this.setTitle(title + tc.ruta);
        }
    }                                       

    private void TEXTOKeyReleased(java.awt.event.KeyEvent evt) {                                  
        
    }                                 

    private void smAcercaActionPerformed(java.awt.event.ActionEvent evt) {                                         
        TEXTO.setText("PROYECTO  FINAL LENGUAJES DE PROGRAMACI\u00F3N - UNAL 2016 \n JORGE SOLANO - MIGUEL BORJA");
    }                                        
    
    FileManager tc = new FileManager();
    Boolean isnew = true;
    String title = "OptiCode";
    
    public javax.swing.JTextArea TEXTO;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenu jMenu2;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JMenuItem smAcerca;
    private javax.swing.JMenuItem smSave1;

}
