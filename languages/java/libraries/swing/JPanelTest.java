import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class JPanelTest {
    public static void main(String[] args) {
        JFrame frame = new FrameAsMethod("JPanel Test", 480, 360);
        frame.setLayout(null);

        JPanel redPanel = new JPanel();
        redPanel.setBackground(Color.RED);
        frame.add(redPanel);
        redPanel.setBounds(20,20,32,128);
        
        JPanel bluePanel = new JPanel();
        bluePanel.setBackground(Color.BLUE);
        frame.add(bluePanel);
        bluePanel.setBounds(40,60,64,64);
        
        JPanel greenPanel = new JPanel();
        greenPanel.setBackground(Color.GREEN);
        frame.add(greenPanel);
        greenPanel.setBounds(420,20,32,128);
    }
}