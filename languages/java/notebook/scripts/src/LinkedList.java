import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


// A list with only linear access (like a dictionary).
public class LinkedList {


    Node head = null;  // the first node of the list
    Node tail = null;
    
    
    LinkedList() {
        this.head = null;  // set the head to null
        this.tail = null;  // set the head to null
    }


    /**
     * Set the first head of the list
     */
    public boolean setHead(String value) {
        if (this.head == null) {  // set the head to the new node
            this.head = new Node(value);
            this.tail = this.head;
            return true;
        } else return false;
    }


    /**
     * Generate the list of nodes from the head to the tail
     * @return the list of nodes
     */
    public List<String> getList() {           
        List<String> nodes = new ArrayList<String>();  // create a new list of nodes
        Node current = this.tail;  // set the second node as the current 
        
        // System.out.println(this.tail.links[1].value);
        while (current.getLink(1) != null) {  // while the current node has a next node (not the last node)
            nodes.add(current.getValue());
            current = current.getLink(1);
        }
        nodes.add(current.getValue());  // Add the last element

        return nodes;
    }


    // to string
    public String toString() {
        return this.getClass().getSimpleName() + ":  ";
    }


    public void describe() {
        System.out.println("\n" + this.getClass().getSimpleName() +  " " + this.getList() + "\n    " + this.toString() + "\n");
    }


    // getters 
    public Node getHead() {return this.head;}
    
    public Node getTail() {return this.tail;}


    // ? LINEAR LIST [][][][][][][][][][][][][][][][][][][][][][[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

    public class LinearList extends LinkedList {


        public LinearList() {
            super();
        }


        /**
         * Add a head to the list. Also adds the link from the 
         * @param value
         */
        public void addHead(String value) {
            if (super.setHead(value) == false) {
                Node newHead = new Node(value);
                super.head.addLink(newHead, 1);  // prev -> head
                super.head = newHead;  // update the head
            }
        }


        @Override
        public String toString() {
            List<String> nodes = super.getList();  // get the list of nodes
            return super.toString() + nodes.stream().map(Object::toString).collect(Collectors.joining(" -> "));
        }
    

    }


    // ? DOUBLE LINKED LIST [][][][][][][][][][][][][][][][][][][][][][[][][][][][][][][][][][][][][][][][][][][][][][][][][][]

    public class DoubleLinkedList extends LinearList {


        public DoubleLinkedList() {
            super();
        }


        public void addHead(String value) {
            if (super.setHead(value) == false) {
                Node newHead = new Node(value);
                newHead.addLink(super.head, 0);  // head <- prev
                super.head.addLink(newHead, 1);  // prev -> head
                super.head = newHead;  // update the head
            }
        }


        @Override
        public String toString() {
            super.toString();
            List<String> nodes = super.getList();  // get the list of nodes
            return nodes.stream().map(Object::toString).collect(Collectors.joining(" <-> "));
        }
    

    }


    // ? CIRCULAR LINKED LIST [][][][][][][][][][][][][][][][][][][][][][[][][][][][][][][][][][][][][][][][][][][][][][][][][]

    // This class is must the same as a double linked list, but the last node must point to the first node
    public class CircularLinkedList extends DoubleLinkedList {


        public CircularLinkedList() {
            super();
        }


        public void addHead(String value) {
            super.addHead(value);
            // connect the head with the tail
        }


        @Override
        public String toString() {
            return super.toString() + " <-> " + super.tail.getValue();
        }


    }


}
