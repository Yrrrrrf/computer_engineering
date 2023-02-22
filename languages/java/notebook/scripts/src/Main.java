/**
 * Tarea 2
 * 
 * 
 * 2120019
 * Reza Campos Fernando Bryan
 */




class Main {

    public static void main(String[] args) {
        System.out.println("\u001B[32mHello World\u001B[0m");  // print hello world in green

		// test linear list
		LinkedList.LinearList animals = new LinkedList().new LinearList();  // create a new list (LinearList)
		// LinkedList.DoubleLinkedList animals = new LinkedList().new DoubleLinkedList();  // create a new list (DoubleLinkedList)
		// LinkedList.CircularLinkedList animals = new LinkedList().new CircularLinkedList();  // create a new list (CircularLinkedList)


		animals.addHead("Dog");  // add a new node at the beginning of the list
		animals.addHead("Bee");  // add a new node at the beginning of the list
		// animals.addHead("Siuuu");  // add a new node at the beginning of the list
		// animals.addHead("Cat");  // add a new node at the beginning of the list
		animals.addHead("Elf");  // add a new node at the beginning of the list
		// System.out.println("\n" + animals.toString());  // print the list
		animals.describe();  // print the list

	}
}
