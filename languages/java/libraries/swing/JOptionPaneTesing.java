import javax.swing.JOptionPane;

public class JOptionPaneTesing {
    public static void main(String[] args) {
        
        // JOptionPane.showMessageDialog(null, "Useless info", "Information Message", JOptionPane.INFORMATION_MESSAGE);
        // JOptionPane.showMessageDialog(null, "Some message", "Plain Message", JOptionPane.PLAIN_MESSAGE);
        // JOptionPane.showMessageDialog(null, "hi?", "Question Message", JOptionPane.QUESTION_MESSAGE);
        // JOptionPane.showMessageDialog(null, "I warn you", "Warning Message", JOptionPane.WARNING_MESSAGE);
        // JOptionPane.showMessageDialog(null, ">:( ERROR", "Error Message", JOptionPane.ERROR_MESSAGE);
        
        // JOptionPane.showConfirmDialog(null, ">:( ERROR", "Yes No Cancel", JOptionPane.YES_NO_CANCEL_OPTION);
        // JOptionPane.showConfirmDialog(null, ">:( ERROR", "Yes No", JOptionPane.YES_NO_OPTION);
        // JOptionPane.showConfirmDialog(null, ">:( ERROR", "Ok Cancel", JOptionPane.OK_CANCEL_OPTION);

        // JOptionPane.showInputDialog(null, "Input Dialog Testing. Hi");
    
        JOptionPane.showOptionDialog(null, "Testing Option Dialog", "Option Dialog", JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE, null, null, null);
    
    }
}
