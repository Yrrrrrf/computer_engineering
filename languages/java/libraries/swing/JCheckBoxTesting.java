import javax.swing.JCheckBox;
import javax.swing.plaf.DimensionUIResource;
import javax.swing.plaf.FontUIResource;

import java.awt.FlowLayout;

public class JCheckBoxTesting {
    public static void main(String[] args) {
        
        FrameAsMethod frame = new FrameAsMethod("JCheckBox", 720, 480);
        frame.setLayout(new FlowLayout());

        JCheckBox checkBox = new JCheckBox("Checkbox");
        checkBox.setFocusable(false);
        checkBox.setPreferredSize(new DimensionUIResource(240,120));
        checkBox.setFont(new FontUIResource("MV Boli", FontUIResource.BOLD, 32));

        // checkBox.addActionListener(e -> System.out.println(checkBox.getAction()));

        frame.add(checkBox);
        frame.pack();
    }
}