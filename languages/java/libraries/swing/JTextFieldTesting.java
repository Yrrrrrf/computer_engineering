import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.plaf.DimensionUIResource;
import java.awt.FlowLayout;

public class JTextFieldTesting {
    public static void main(String[] args) {
        
        FrameAsMethod frame = new FrameAsMethod("JTextField Testing", 720, 480);
        
        frame.setLayout(new FlowLayout());

        JTextField textField = new JTextField();
        textField.setPreferredSize(new DimensionUIResource(240, 40));

        JButton button = new JButton("Sumbit");
        button.setPreferredSize(new DimensionUIResource(80, 40));
        button.addActionListener(e -> System.out.println("Welcome: " + textField.getText()));

        frame.add(textField);
        frame.add(button);
        frame.pack();
    }
}