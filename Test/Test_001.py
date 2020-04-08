class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the middle of the linked list
    def printMiddle(self):
        single = self.head
        double = self.head

        if self.head is not None:
            while (double is not None and double.next is not None):
                double = double.next.next
                single = single.next
            print("The middle element is: ", single.data)
            # I am not able to get the list to remove the middle node correctly.
            # I know that the previous nodes pointer is updated to point to the
            # .next.next node and the node I am removing is pointed to null.
            # single.val = single.next.val
            # single.next = single.next.next

            # Driver code


list1 = LinkedList()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.printMiddle()
