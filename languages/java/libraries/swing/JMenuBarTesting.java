import javax.swing.ImageIcon;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

import java.awt.FlowLayout;
import java.awt.Image;
import java.awt.event.KeyEvent;

public class JMenuBarTesting {
    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JMenuBar Testing", 720, 480);
        frame.setLayout(new FlowLayout());

        JMenuBar menuBar = new JMenuBar();

        JMenu menu1 = new JMenu("1");
        JMenu menu2 = new JMenu("2");
        JMenu menu3 = new JMenu("3");

        JMenuItem item11 = new JMenuItem("Exit");
        JMenuItem item12 = new JMenuItem("12");
        JMenuItem item13 = new JMenuItem("13");
        // RESIZE IMAGE
        menu1.setIcon(new ImageIcon(new ImageIcon("src/images/books.png").getImage().getScaledInstance(20, 20, Image.SCALE_DEFAULT)));
        
        // Press to Exit
        item11.addActionListener(e -> System.exit(0));
        // Exit using E key
        item11.setMnemonic(KeyEvent.VK_E);

        menu1.add(item11);
        menu1.add(item12);
        menu1.add(item13);

        menuBar.add(menu1);
        menuBar.add(menu2);
        menuBar.add(menu3);

        frame.setJMenuBar(menuBar);
        frame.setVisible(true);
    }
}
