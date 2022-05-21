package visualalgo.views;

import javax.swing.JButton;
import javax.swing.JPanel;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;

public class AlgorithmOptions extends JPanel {
    
    private JButton DJ;
    private JButton breadth;
    private JButton depth;

    public AlgorithmOptions(){

        this.setLayout(new FlowLayout());

        this.DJ = new JButton("Djikstra's Algorithm");
        this.breadth = new JButton("Breadth-First Search");
        this.depth = new JButton("Depth-First Search");

        this.add(DJ);
        this.add(breadth);
        this.add(depth);
    }

    public void addDJListener(ActionListener actionListener)
    {
       DJ.addActionListener(actionListener);
    }
 
    public void addBreadthListener(ActionListener l)
    {
       breadth.addActionListener(l);
    }
 
    public void addDepthListener(ActionListener l)
    {
       depth.addActionListener(l);
    }
}
