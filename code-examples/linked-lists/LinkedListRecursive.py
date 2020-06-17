# Author: Elaine Laguerta
# Description: A LinkedList class with recursive implementations of the add, display, remove,
# contains, insert, and reverse methods.

class Node:
    """
    Represents a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self, node = None):
        """
        :param node: Optional parameter, the node that the head of the list will point to.
        Default value is none.
        """
        self.head = node

    def add(self, val):
        """
        Adds a node containing val to the linked list, by recursion
        """
        if self.head is None:
            # If the list is empty, create a new Node with data equal to val,
            # and set the head of the list to point to the new node
            self.head = Node(val)
        else:
            # otherwise, create a list, "next_list", with head pointing to the next node
            # and add the value to "next_list"
            next_list = LinkedList(self.head.next)
            next_list.add(val) # recursive call on next_list
            self.head.next = next_list.head

    def display(self, delim = " "):
        """
        Prints out the values in the linked list.
        Values are printed on the same line separated by delim.
        :param delim: Optional string parameter that delimits the values for printing
        Default value is a single space. Note that the delim string will be printed after the final element.
        """

        if self.head is None:
            # if the list is empty, call print with no arguments,
            # which will print a new line to the console.
            print()
        else:
            # otherwise, print the data at the head node
            # make a new list with head pointing to the next node, tell the new list to display itself
            print(self.head.data, end = delim)
            next_list = LinkedList(self.head.next)
            next_list.display() # recursive call on next_list

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self.head is None:  # If the list is empty
            return

        if self.head.data == val:  # If the node to remove is the head
            self.head = self.head.next
        else:
            # otherwise, make a new list, "next_list", with head pointing to the next node
            # recursively remove the value from "next_list"
            # then point this list's head.next node to the head of next_list
            next_list = LinkedList(self.head.next)
            next_list.remove(val) # recursive call on next_list
            self.head.next = next_list.head

    def contains(self, value):
        """
        Recursively searches the LinkedList for value.
        :param value: Value to search for
        :return: True if the linked list contains the value, False otherwise
        """
        if self.head is None:
            # if this list is empty, it contains no values. Return False.
            return False
        elif self.head.data == value:
            # First, check the head of the list. If the head contains value,
            # return True
            return True
        else:
            # Otherwise, create a new list, next_list, with head pointing to this list's next node.
            # Search next_list for the value and return the result.
            next_list = LinkedList(self.head.next)
            return next_list.contains(value) # recurisve call on next_list

    def insert(self, val, pos):
        """
        Recursively inserts val at position pos in the linked in.
        The first position is pos = 0.
        :param val: Value to insert.
        :param pos: Position in the linked list
        """
        if pos == 0:
            # if we want to insert at position 0, the beginning of the list
            # create a new node with data equal to val. Point this new node's next to the
            # current head of the list. Then, point this list's head to the new node.
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
        else:
            # otherwise, create a new list, next_list, with head pointing to this
            # list's head.next. Insert the value in next_list at position pos - 1.
            # set this list's head.next to next_list.head
            next_list = LinkedList(self.head.next)
            next_list.insert(val, pos - 1) # recursive call on next_list
            self.head.next = next_list.head

    def reverse(self):
        """
        Recursively reverses the list by appending the first element to the end
        of the reversal of the rest of the list.
        :return: No return value
        """
        if self.head == None:
            # if the list is empty, it is already the reversal of itself. Return.
            return
        elif self.head.next == None:
            # if the list has one element, it is already the reversal of itself. Return.
            return
        else:
            # if the list has two or more elements, make a new list, new_list, with head pointing
            # to this list's head.next. Reverse new_list. Add this list's first element
            # to the end of the reversed new_list.
            new_list = LinkedList(self.head.next)
            last_val = self.head.data
            new_list.reverse() # recursive call on new_list
            new_list.add(last_val)
            self.head = new_list.head


if __name__ == "__main__":
    """
    Test code
    """
    # test add, display, remove, conains
    my_list = LinkedList()
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    my_list.display() # 1 2 3 4
    my_list.remove(2)
    my_list.remove(1)
    my_list.remove(4)
    my_list.remove(100)
    my_list.display()  # 3
    my_list.remove(3)
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
    my_list.add(4)
    print(my_list.contains(1)) # True
    print(my_list.contains(3)) # True
    print(my_list.contains(5)) # False
    # test insert
    my_list.insert(-2, 2)
    my_list.display() # 1 2 -2 3  4
    my_list.reverse()
    my_list.display() # 4 3 -2 2 1
    # test edge cases of reverse
    a_list = LinkedList()
    a_list.reverse()
    a_list.add(1)
    a_list.reverse()
    a_list.display() # 1
