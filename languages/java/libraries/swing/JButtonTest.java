import javax.swing.JButton;
import javax.swing.JLabel;

// import java.awt.event.ActionEvent;
// import java.awt.event.ActionListener;

public class JButtonTest {

    JButton button = new JButton();

    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JButton Test", 720, 480);
        frame.setLayout(null);
        // Just to add a text in the button
        JLabel label = new JLabel();
        label.setText("Simple Button");
        //Creating the button
        JButton button = new JButton();
        button.setBounds(20,20,120,40);
         
        button.add(label); // Add label to the button
        frame.add(button); // The the button to the frame
        
        //? Implement action using lambda expression 
        // With is is not necessary to import the ActionListener/ActionEvent
        button.addActionListener(e -> System.out.println("Button Pressed"));

    }

}