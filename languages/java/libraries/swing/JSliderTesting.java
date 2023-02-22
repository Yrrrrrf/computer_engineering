import javax.swing.JSlider;
import javax.swing.SwingConstants;
import javax.swing.plaf.DimensionUIResource;
import javax.swing.plaf.FontUIResource;

public class JSliderTesting {
    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JSlider Testing", 780, 180);

        JSlider slider = new JSlider(0,100, 40);
        slider.setPreferredSize(new DimensionUIResource(240, 720));
        
        slider.setPaintTicks(true);
        slider.setMinorTickSpacing(10);
        
        slider.setPaintTrack(true);
        slider.setMajorTickSpacing(25);
        
        slider.setPaintLabels(true);
        slider.setFont(new FontUIResource("MV Boli", FontUIResource.BOLD, 12));

        slider.setOrientation(SwingConstants.VERTICAL);
        // ADD CHANGE LISTENER
        slider.addChangeListener(e -> System.out.println(slider.getValue()));

        frame.add(slider);
        frame.pack();
    }
}