import javax.swing.JLayeredPane;
import javax.swing.JPanel;
import javax.swing.plaf.ColorUIResource;

import java.awt.Color;

public class JLayeredPaneTesting {
    public static void main(String[] args) {

        FrameAsMethod frame = new FrameAsMethod("JLayeredPane Testing", 720, 480);

        JLayeredPane layeredPane = new JLayeredPane();
        layeredPane.setBounds(0, 0, frame.getWidth(), frame.getHeight());
        
        layeredPane.setBackground(Color.BLACK);
        layeredPane.setOpaque(true);

        JPanel panel1 = new JPanel();
        panel1.setBackground(ColorUIResource.RED);
        panel1.setBounds(0, 0, 200, 200);

        JPanel panel2 = new JPanel();
        panel2.setBackground(ColorUIResource.GREEN);
        panel2.setBounds(100, 100, 200, 200);

        JPanel panel3 = new JPanel();
        panel3.setBackground(ColorUIResource.BLUE);
        panel3.setBounds(200, 200, 200, 200);
        
        layeredPane.add(panel1, Integer.valueOf(0));
        layeredPane.add(panel2, Integer.valueOf(1));
        layeredPane.add(panel3, Integer.valueOf(1));
        
        frame.add(layeredPane);
    }
}