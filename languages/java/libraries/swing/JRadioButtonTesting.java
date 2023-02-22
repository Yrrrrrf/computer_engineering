import java.awt.FlowLayout;

import javax.swing.ButtonGroup;
import javax.swing.JRadioButton;

public class JRadioButtonTesting {
    public static void main(String[] args) {

        FrameAsMethod frame = new FrameAsMethod("JCheckBox", 720, 480);
        frame.setLayout(new FlowLayout());

        JRadioButton option1 = new JRadioButton("One");
        JRadioButton option2 = new JRadioButton("Two");
        JRadioButton option3 = new JRadioButton("Tri");
        // Action Listener using Functional Paradigm
        option1.addActionListener(e -> System.out.println("You selected 1"));
        option2.addActionListener(e -> System.out.println("You selected 2"));
        option3.addActionListener(e -> System.out.println("You selected 3"));

        ButtonGroup group = new ButtonGroup();
        group.add(option1);
        group.add(option2);
        group.add(option3);

        frame.add(option1);
        frame.add(option2);
        frame.add(option3);

        frame.pack();
        
    }
}