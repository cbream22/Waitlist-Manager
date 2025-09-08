class Node:
    def __init__(self, name: str):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name: str) -> str:
        """Add a customer to the front (VIP)."""
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        return f"{name} added to the front of the waitlist"

    def add_end(self, name: str) -> str:
        """Add a customer to the end (general)."""
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return f"{name} added to the end of the waitlist"
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name: str) -> str:
        """Remove the first occurrence of name from the list."""
        if not self.head:
            return f"{name} not found"

        # If head is the node to remove
        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        prev = self.head
        current = self.head.next
        while current:
            if current.name == name:
                prev.next = current.next
                return f"Removed {name} from the waitlist"
            prev = current
            current = current.next

        return f"{name} not found"

    def print_list(self) -> None:
        """Print the list in order from head to tail."""
        if not self.head:
            print("The waitlist is empty")
            return
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_manager():
    waitlist = LinkedList()

    try:
        while True:
            print("\n--- Waitlist Manager ---")
            print("1. Add customer to front")
            print("2. Add customer to end")
            print("3. Remove customer by name")
            print("4. Print waitlist")
            print("5. Exit")
            choice = input("Choose an option (1–5): ").strip()

            if choice == "1":
                name = input("Enter customer name to add to front: ").strip()
                print(waitlist.add_front(name))

            elif choice == "2":
                name = input("Enter customer name to add to end: ").strip()
                print(waitlist.add_end(name))

            elif choice == "3":
                name = input("Enter customer name to remove: ").strip()
                print(waitlist.remove(name))

            elif choice == "4":
                waitlist.print_list()

            elif choice == "5":
                print("Exiting waitlist manager.")
                break

            else:
                print("Invalid option, please choose 1–5.")
    except KeyboardInterrupt:
        print("\nExiting waitlist manager (keyboard interrupt).")


if __name__ == "__main__":
    waitlist_manager()

'''
Design Memo: 
This program manages a customer waitlist using a linked list implementation. 
Each customer is represented by a Node that stores the customer’s name and a pointer 
to the next node in the list. The LinkedList class holds the head pointer, which 
references the first node (the front of the waitlist).

The head is the entry point to the structure: traversals, removals, and insertions all 
start from the head. Adding to the front creates a new Node whose next points to the prior 
head, then updates head to the new node in an O(1) operation. Adding to the end 
requires traversing the list to find the last node, then linking the new node; this 
is on in the general case. Removing a node requires careful pointer updates: if the 
node is the head, head is updated to head.next; otherwise, the previous node’s next 
skips the removed node.

A real engineer might build a custom linked list when they need fine-grained control 
over insertion and removal semantics or when working in low-level systems where 
contiguous memory arrays are undesirable. For example, ticketing systems may need to 
insert VIP customers at the front quickly, while ordinary customers queue at the end. 
Custom lists also enable specialized behavior like skipping specific nodes or maintaining 
extra metadata per node without relying on higher-level abstractions.
'''
