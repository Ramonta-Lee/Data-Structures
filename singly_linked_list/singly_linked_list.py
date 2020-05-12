class Node:
    def __init__(self, value=None, next_node=None):
     # the value at this linked list node
        self.value = value
     # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's "next_node" reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None 


    def add(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # value is actual value, and hasn't been wrapped in a Node yet

        # what if the list is empty?
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # we want to add it to the last node in the list
            # we can get to the last node in the list by traversing it
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list
            current.set_next(new_node)

    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            # this stores the value of the head in a variable
            value = self.head.get_value()
            # need to remove the value at the head
            # need to update the value at self.head; head needs to refer to something
            # self.head.get_next(): moves the Head pointer to the second node in the chain. 
            # The head is how we access the Node at position  0 or 1, we then cut that off. 
            # storing it in the value and then returning the value allows us 
            self.head = self.head.get_next()
            return value

    def add_to_head(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def add_to_tail(self, value):
        node = Node(value)
        node.