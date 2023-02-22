import java.awt.Font;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.border.Border;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.FontUIResource;

public class JFrameTesting extends JFrame {
    public static void main(String[] args) throws Exception {
        JFrame frame = new JFrame();
        frame.setTitle("JFrame Testing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        frame.setSize(720,480) ;
        // frame.setResizable(false);
        
        ImageIcon windowIcon = new ImageIcon("images/books.png");
        frame.setIconImage(windowIcon.getImage());
        
        // frame.getContentPane().setBackground(new ColorUIResource(48,48,48));
        
        ImageIcon textIcon = new ImageIcon("images/writting.png");

        JLabel label = new JLabel();
        label.setIcon(textIcon);
        label.setText("Some text");

        //? Change the text location in relation to the image
        label.setHorizontalTextPosition(JLabel.RIGHT);
        label.setVerticalTextPosition(JLabel.CENTER);
    
        //? Change label elements location
        label.setHorizontalAlignment(JLabel.LEFT);
        label.setVerticalAlignment(JLabel.TOP);

        //? Change text config
        label.setForeground(new ColorUIResource(255,0,0));
        label.setFont(new FontUIResource("MV Boli", Font.BOLD, 32));

        label.setIconTextGap(50);

        label.setBackground(new ColorUIResource(0,0,0));
        label.setOpaque(true);

        //? Border
        Border border = BorderFactory.createLineBorder(new ColorUIResource(0,255,0), 5);
        label.setBorder(border);

        //? Changing layout settings
        frame.setLayout(null);
        //? We need to add the label Bounds to put it in the Window
        label.setBounds(20, 20, 670, 240);

        frame.setVisible(true);
        frame.add(label);
    }
}