import javax.swing.JComboBox;
import javax.swing.plaf.DimensionUIResource;

import java.awt.FlowLayout;

public class JComboBoxTesting {
    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JComboBox", 720, 480);
        frame.setLayout(new FlowLayout());

        String[] animals = {"dog", "cat", "lion", "bear", "panda"};
        JComboBox<String[]> comboBox = new JComboBox<String[]>();
        comboBox.addItem(animals);

        comboBox.setPreferredSize(new DimensionUIResource(240, 80));

        comboBox.setEditable(true);

        comboBox.addActionListener(e -> System.out.println(comboBox.getSelectedItem()));

        frame.add(comboBox);
        frame.pack();
    }
}