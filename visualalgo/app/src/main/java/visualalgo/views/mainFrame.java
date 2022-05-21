package visualalgo.views;

import java.awt.Dimension;

import javax.swing.JFrame;

import visualalgo.controllers.AlgorithmController;

public class mainFrame extends JFrame{

    AlgorithmController controller;
    final int frameSize;
    
    public mainFrame(AlgorithmController control){
        
        this.setTitle("Algorithm Visualizer");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);

        this.controller = control;
        frameSize = 400;

        this.setPreferredSize(new Dimension(frameSize*2, frameSize*2));

        this.add(new Home(controller, frameSize));

    }
}
