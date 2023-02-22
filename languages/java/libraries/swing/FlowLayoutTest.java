import javax.swing.JButton;
import javax.swing.JLabel;

import java.awt.FlowLayout;

public class FlowLayoutTest {

    static public JButton createButton(String number, FrameAsMethod frame) {
        JButton button = new JButton(); 
        JLabel label = new JLabel();
        label.setText(number);
        button.add(label);
        frame.add(button);

        return button;
    }


    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("Flow Layout Test", 720, 480);

        frame.setLayout(new FlowLayout());

        for (int i = 0; i < 10; i++) createButton("" + i, frame);

        frame.pack();

    }
}
