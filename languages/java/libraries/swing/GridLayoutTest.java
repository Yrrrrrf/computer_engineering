import java.awt.GridLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JLabel;

public class GridLayoutTest {

    static public JButton createButton(String text, Color color, FrameAsMethod frame) { //, Object constranints) {
        JButton button = new JButton();
        JLabel label = new JLabel();
        label.setText(text);
        button.add(label);
        
        //? Change label elements location
        label.setHorizontalAlignment(JLabel.RIGHT);
        label.setVerticalAlignment(JLabel.BOTTOM);

        label.setForeground(Color.WHITE);
        label.setFont(new Font("MV Boli", Font.BOLD, 32));

        button.setBackground(color);
        button.setPreferredSize(new Dimension(120, 120));
        // frame.add(button, constranints);
        frame.add(button);

        return button;
    }


    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("Grid Layout Test", 1080, 480);

        frame.setLayout(new GridLayout(2,3));

        // JButton panel1 = createButton("1", Color.BLACK, frame);
        // JButton panel2 = createButton("2", Color.BLUE  , frame);
        // JButton panel3 = createButton("3", Color.YELLOW, frame);
        // JButton paneL4 = createButton("4" , Color.RED   , frame);
        // JButton panel5 = createButton("5" , Color.GREEN , frame);
        // JButton panel6 = createButton("6" , Color.ORANGE , frame);

    }
}