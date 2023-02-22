/**
 * Structure that stores a value.
 */
public class Node {
   

    private String value;  // value of the node

    private Node[] links = new Node[2];  // the list contains the next nodes of the current node


    // constructor
    public Node(String value) {
        this.value = value;
    }


    /**
     * Add a {@code Node} to the list of links (always at the index 0)
     * @return the node that was added
     */
    public Node addLink(Node node) {
        
        links[0] = node;  // add the node to the list of links (at the end of the list)
        System.out.println(this.value + " -> " + node.getValue());
        return node;
    }


    /**
     * Add a {@code Node} to the list of links
     * @return the node that was added
     */
    public Node addLink(Node node, int index) {

        links[index] = node;  // add the node to the list of links (at the end of the list)
        System.out.println(this.value + " -> " + node.getValue());
        return node;
    }


    /**
     * Remove a {@code Node} from the list of links
    * @param node
     */
    public void removeLink(Node node) {
        System.out.println("Removing link to " + node.getValue());
        for (int i = 0; i < links.length; i++) {  // look if node is in the list of links
            if (links[i] != null) if (links[i].getValue().equals(node.getValue())) links[i] = null;
        }
    }


    // toString
    @Override
    public String toString() {
        // return a string in the form backward -> current -> forward
        return "Node:  " + links[0].getValue() + " -> " + value + " -> " + links[1].getValue() + "\n";
    }



    // ? getters ------------------------------------------------------------------------------------------------------------------
    
    /**
     * Get the stored value of the node
     * @return value
     */
    public String getValue() {
        return value;
    }
    

    /**
     * Get the list of nodes that the current link is pointing to.
     * <p>
     * this -> node_0, node_*, ...
     * @return List of nodes
     */
    public Node[] getLinks() {
        return links;
    }


    /**
     * Get the node at the specified index
     * @param index
     * @return
     */
    public Node getLink(int index) {
        return links[index];
    }

    
    // ? setters ------------------------------------------------------------------------------------------------------------------

    /**
     * Set the value that the node will store
     * @param value new value
     */
    public void setValue(String value) {
        this.value = value;
    }


}

