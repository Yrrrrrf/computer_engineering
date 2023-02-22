import javax.swing.ImageIcon;
import javax.swing.JFrame;

// import java.awt.event.ActionEvent;
// import java.awt.event.ActionListener;

// public class FrameAsMethod extends JFrame implements ActionListener {
public class FrameAsMethod extends JFrame {

    FrameAsMethod(String title, int width, int height){
        this.setTitle(title);
        this.setVisible(true);
        this.setSize(width, height);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        ImageIcon icon = new ImageIcon("images/books.png");
        this.setIconImage(icon.getImage());
    }

    // @Override
    // public void actionPerformed(ActionEvent e) {
    // }
}
