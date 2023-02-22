import javax.swing.JProgressBar;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.FontUIResource;

public class JProgressBarTesting {
    public static void main(String[] args) {
        FrameAsMethod frame = new FrameAsMethod("JProgressBar Testing", 480, 100);
        frame.setLayout(null);

        JProgressBar progressBar = new JProgressBar();
        progressBar.setBounds(0,0,480,40);        
        progressBar.setStringPainted(true);
        // progressBar.setString("progress " + progressBar.getValue() + "%");

        progressBar.setBackground(ColorUIResource.GRAY);
        progressBar.setFont(new FontUIResource("MV Boli", FontUIResource.BOLD, 16));
        progressBar.setForeground(ColorUIResource.BLUE); // 

        frame.add(progressBar);

        progressBar.setValue(0);
        for (int i = 0; i <= 100; i++)
            try {
                progressBar.setValue(i);
                progressBar.setString("progress " + progressBar.getValue() + "%");
                Thread.sleep(100/2);
            } catch (Exception e) {e.printStackTrace();}
        progressBar.setString("DONE!");

        try {
            Thread.sleep(1000);
            System.exit(0);
        } catch (Exception e) {}

    }
}