package visualalgo.views;
import visualalgo.controllers.AlgorithmController;

import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Home extends JPanel{
    
    final int frameSize;

    AlgorithmController controller;


    public Home(AlgorithmController control, int size){

        this.controller = control;
        this.frameSize = size;

        this.setLayout(new BorderLayout());

        AlgorithmOptions options = new AlgorithmOptions();
        this.add(options, BorderLayout.PAGE_START);
        options.addDJListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
                // implement controller begin dj
            }
         });

         options.addBreadthListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
                // implement controller begin breadth 
            }
         });

         options.addDepthListener(new ActionListener(){
            public void actionPerformed(ActionEvent e)
            {
                // implement controller begin depth
            }
         });

         

    }
}
