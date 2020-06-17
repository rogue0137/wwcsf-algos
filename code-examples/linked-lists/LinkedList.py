
class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data9
        self.next = None

class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self.head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self.head is None:  # If the list is empty
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.head is None:  # If the list is empty
            return

        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next
        else:
            current = self.head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self.head is None

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            else:
                current = current.next
        return False

    def insert(self, val, pos):
        index = 0
        prev = None
        current = self.head
        while index < pos and current is not None:
            prev = current
            current = current.next
            index += 1
        # now index = pos or current node is None. Insert the element
        temp = current
        this_node = Node(val)
        if prev is None:
            self.head = this_node
        else:
            prev.next = this_node
        this_node.next = temp

    def reverse(self):
        prev = None
        current = self.head
        next = current.next
        # prev current next #
        # None 1 2 #
        while next is not None:
            temp = next.next    # 3, 4, None
            next.next = current # 2 -> 1,  3 ->2, 4 -> 3,
            current.next = prev # 1 -> None, 2-> 1, 3-> 2,
            prev = current  # prev = 1, prev = 2, prev = 3
            current = next # current = 2, current = 3, current = 4
            next = temp    # next = 3, next = 4, next = None
        self.head = current



if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    print(my_list.contains(1))
    print(my_list.contains(3))
    print(my_list.contains(5))
    my_list.display()
    my_list.insert(-2, 2)
    my_list.display()
    my_list.reverse()
    my_list.display()
