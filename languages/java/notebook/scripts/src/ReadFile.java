import java.io.File;  // Provide a general class for file and directory pathnames
import java.io.FileNotFoundException;  // Allow to catch the exception if the file is not found
import java.io.PrintWriter;  // Allow to write to a file
import java.util.Scanner;  // Allow to read from a file (or the console)


/**
 * Contains the main methods (CRUD operations) to manage a file and it's data as a LinkedList
 */
public class ReadFile {


    /**
     * Create a new file in the current directory
     * @param filename
     * @return
     */
    public static boolean createFile(String filename) {
        File file = new File(filename);
        try {
            if (file.createNewFile()) {  // Create a new file
                System.out.println("File created: " + file.getName());  // Print the name of the file
                return true;  // Return true if the file is created
            } else {
                System.out.println("File already exists.");  // Print the name of the file
                return false;  // Return false if the file already exists
            }
        } catch (Exception e) {  // Catch the exception if the file is not created
            e.printStackTrace();  // Print the error
            return false;  // Return false if the file is not created
        }
    }


    /**
     * Read a file and print it
     * <p>
     * Read a file and return the data as a String
     * @param filename
     * @return file_data
     */
    public static String readFile(String filename) {
        File file = new File(filename);
        String file_data = "";  // Initialize the file data
        try (Scanner scanner = new Scanner(file)) {  // Create a Scanner object to read the file
            // read lines and endlines
            while (scanner.hasNextLine()) file_data += scanner.nextLine() + "\n";  // Read the file line by line
            System.out.println(file_data);  // Read the file line by line
        } catch (FileNotFoundException e) {  // Catch the exception if the file is not found
            e.printStackTrace();  // Print the error
            return null;  // Return false if the file is not found
        }
        return file_data;  // Return true if the file is found
    }


    /**
     * Update a file with the given name
     * <p>
     * Add a new line using the console (Scanner)
     * @param filename
     */
    public static void addLine(String filename) {
        String file_data = readFile(filename);  // Read the file
        
        try (Scanner scanner = new Scanner(System.in)) {  // Create a Scanner object to read the file
            System.out.println("Enter the new line: ");  // Ask the user for the new line
            file_data += scanner.nextLine();  // Add the new line to the file
            // update test.txt from current directory
            updateFile(filename, file_data);  // Save the new data to the file
        } catch (Exception e) {
            System.out.println("Please enter a valid input.\n" + e.getMessage());
       }
    }


    /**
     * Update a file with the given name
     * <p>
     * Update the file with the given data
     * @param filename
     * @param data
     */
    public static void updateFile(String filename, String data) {
        File file = new File(filename);
        try (PrintWriter writer = new PrintWriter(file)) {  // Create a PrintWriter object to write the file
            writer.println(data);  // Write the data to the file
            System.out.println("File updated: " + file.getName());  // Print the name of the file
        } catch (FileNotFoundException e) {  // Catch the exception if the file is not found
            e.printStackTrace();  // Print the error
        }
    }


    /**
     * Delete a file with the given name
     * @param filename
     * @return true if the file is deleted, false if the file is not found
     */
    public static void deleteFile(String filename) {
        File file = new File(filename);
        if (file.delete()) System.out.println("File deleted: " + file.getName());  // Print the name of the file
        else System.out.println("File not found.");  // Print the name of the file
    }


    /**
     * Delete a line from a file with the given name
     * @param filename
     * @return true if the file is deleted, false if the file is not found
     */
    // public static void deleteLine(String filename) {
    //     String file_data = readFile(filename);  // Read the file
    //     String[] lines = file_data.split("\n");  // Split the file data by lines 
    // }    

}
