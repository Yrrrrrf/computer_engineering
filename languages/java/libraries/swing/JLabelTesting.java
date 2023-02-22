import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.border.Border;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.FontUIResource;

public class JLabelTesting {
    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JLabel Testing" , 720, 480);
        // i don't know where to start the image icon path :/
        // sometimes works with src, sometimes withiout it :/ just luck
        ImageIcon textIcon = new ImageIcon("src/images/writting.png");

        JLabel label = new JLabel();
        label.setIcon(textIcon);
        label.setText("Some text");

        //? Change the text location in relation to the image
        label.setHorizontalTextPosition(JLabel.RIGHT);
        label.setVerticalTextPosition(JLabel.CENTER);
    
        //? Change label elements location
        label.setHorizontalAlignment(JLabel.RIGHT);
        label.setVerticalAlignment(JLabel.BOTTOM);

        //? Change text config
        label.setForeground(new ColorUIResource(255,0,0));
        label.setFont(new FontUIResource("MV Boli", FontUIResource.BOLD, 32));

        label.setIconTextGap(50);

        label.setBackground(new ColorUIResource(0,0,0));
        label.setOpaque(true);

        //? Border
        Border border = BorderFactory.createLineBorder(new ColorUIResource(0,255,0), 5);
        label.setBorder(border);

        //? Changing layout settings
        frame.setLayout(null);
        //? The label needs to be part of the frame to declare it's bounds
        frame.add(label);
        //? We need to add the label Bounds to put it in the Window
        label.setBounds(20, 20, 670, 240);

        frame.setVisible(true);
    }
}
