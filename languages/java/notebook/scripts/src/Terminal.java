import java.util.LinkedList;
import java.util.Scanner;


class Terminal {
    

    /**
     * Asks for an integer and this funciton will only end when the given value were an Integer
     * @param askedValue
     * @return integerNumber
     */
    public static int askInteger(String askedValue) {
        int number = 0;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print(askedValue);
            number = Integer.valueOf(sc.next());
        } catch (Exception e) {
            System.out.println("Please use only numbers");
            number = askInteger(askedValue);
        }
        return number;
    }


	/**
	 * Add a new node to the linked list
	 * @param data
	 */
	public static void addNode() {
		try (Scanner scanner = new Scanner(System.in)) {  // Create a new scanner
			int index = askInteger("Enter the index: ");  // Ask for the index
			System.out.println("Enter the data: ");  // Ask for the data
			String data = scanner.nextLine();  // Get the data
			LinkedList<String> animals = new LinkedList<>();
			animals.add(index + " " + data);
			System.out.println("LinkedList: " + animals);
		}
	}

}
