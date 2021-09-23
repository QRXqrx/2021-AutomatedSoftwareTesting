public class Node {
	int elem;
	Node next;

	Node swapNode() {
		
		if(next!=null) 
			if(elem>next.elem) {
				Node t = next;
				next = t.next;
				t.next=this;
				assert elem < t.next.elem;
				return t;
			}
		return this;
	}

	/* ----- Test Driver ----- */
	public static void main(String[] args) {	
		Node n = new Node();
		Node result =n.swapNode();
	}
}
