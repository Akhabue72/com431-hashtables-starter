from node import Node


class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    # TODO modify "add()" so that it takes a key and a value as parameters and 
    # creates a  tuple using them. The Node should then be created using the 
    # tuple.
    def add(self, key, value):
        n = Node((key, value))
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n

    def get(self, index):
        counter = 0
        current_node = self.first
        while current_node is not None:
            if counter == index:
                return current_node
            else:
                current_node = current_node.next
                counter += 1
        return None
    
    # TODO modify "find()" so that it takes a KEY as a parameter  and searches 
    # the linked list until it finds a tuple with that key. It should then
    # return the value (i.e. the second member of the tuple)
    def find(self, key):
        current_node = self.first
        while current_node is not None:
            if current_node.value[0] == key:
                return current_node.value[1]
            else:
                current_node = current_node.next
        return None
