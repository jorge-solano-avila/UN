import java.io.*;
import java.util.*;
import javax.swing.*;

public class FileManager 
{
	File archivo = null;
	FileReader fr = null;
	BufferedReader br = null;
	FileWriter fichero = null;
	PrintWriter pw = null;
	String ruta = "";

    public FileManager(){}
    
    private String OpenFile(String ruta)
    {
        String t = "";
        try {         
            archivo = new File (ruta);            
            fr = new FileReader (archivo);
            br = new BufferedReader(fr);
            String linea;
            while((linea=br.readLine())!=null)            
                t = t + linea + "\n";
        }
      catch(Exception e){
         e.printStackTrace();
      }finally{         
         try{                    
            if( null != fr ){   
               fr.close();     
            }                  
         }catch (Exception e2){ 
            e2.printStackTrace();
         }
      }
        return t;
    }
    
    private void SaveFile(String t, String ruta){   
    StringTokenizer st = new StringTokenizer(t,"\n");
    try
        {
            fichero = new FileWriter(ruta);
            pw = new PrintWriter(fichero);                               
            while(st.hasMoreTokens()){
                String line = st.nextToken();
                pw.println(line);           
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
           try {           
           if (null != fichero)
              fichero.close();
           } catch (Exception e2) {
              e2.printStackTrace();
           }
        }                
    }
    
    public boolean  Dialog(String Opcion, JTextArea tArea){                
        boolean b=true;
        if (Opcion.equals("Open")){
                JFileChooser fileChooser = new JFileChooser();              
                int result = fileChooser.showOpenDialog(null);  
                if ( result == JFileChooser.APPROVE_OPTION ){            
                    ruta = fileChooser.getSelectedFile().getAbsolutePath(); 
                    tArea.setText(OpenFile(ruta));                                       
                    b=false;
                }
        }
        else if (Opcion.equals("Save As")){
                JFileChooser fileChooser = new JFileChooser();              
                int result = fileChooser.showSaveDialog(null);
                if ( result == JFileChooser.APPROVE_OPTION ){                       
                    ruta = fileChooser.getSelectedFile().getAbsolutePath();                          
                    ruta = ruta + ".txt";
                    SaveFile(tArea.getText() ,ruta);                           
                    b=false;
                }
        }
        else if(Opcion.equals("Save")){
        	
            SaveFile(tArea.getText() ,ruta); 
            b=false;
        }       
        return b;
    }
}
