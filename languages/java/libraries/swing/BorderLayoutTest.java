import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;

import javax.swing.JLabel;
import javax.swing.JPanel;

public class BorderLayoutTest {

    static public JPanel createPanel(String text, Color color, FrameAsMethod frame, Object constranints) {
        JPanel panel = new JPanel();
        JLabel label = new JLabel();
        label.setText(text);
        panel.add(label);
        
        //? Change label elements location
        label.setHorizontalAlignment(JLabel.RIGHT);
        label.setVerticalAlignment(JLabel.BOTTOM);

        label.setForeground(Color.WHITE);
        label.setFont(new Font("MV Boli", Font.BOLD, 32));

        panel.setBackground(color);
        panel.setPreferredSize(new Dimension(120, 120));
        frame.add(panel, constranints);

        return panel;
    }


    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("Border Layout Test", 480, 480);

        frame.setLayout(new BorderLayout());

        // JPanel panel1 = createPanel("Center", Color.BLACK, frame, BorderLayout.CENTER);
        // JPanel panel2 = createPanel("North", Color.BLUE  , frame, BorderLayout.NORTH);
        // JPanel panel3 = createPanel("South", Color.YELLOW, frame, BorderLayout.SOUTH);
        // JPanel paneL4 = createPanel("East" , Color.RED   , frame, BorderLayout.EAST);
        // JPanel panel5 = createPanel("West" , Color.GREEN , frame, BorderLayout.WEST);
    }
}
