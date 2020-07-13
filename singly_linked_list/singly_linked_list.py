class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
        # returns the node's data 
    
    def get_next(self):
        return self.next
        # returns what is pointed at by the node's 'next' reference
    
    def set_next(self, new_next):
        self.next = new_next
        # returns this node's 'next' reference to 'new_next'

class LinkedList:
    def __init__(self):
        self.head = None
        # Above is the first node in LinkedList
        self.tail = None
        # Above is the last node in LinkedList
    
    def add_to_tail(self, value):
        # Created a new Node from the value
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_next()
        v = self.head.get_next()
        return v
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        v = self.tail.get_value()
        self.tail = current
        return v
    
    def contains(self, value):
        if not self.head:
            return False
        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        
        return False
    
    def get_max(self):
        if not self.head:
            return None
        
        max_value = self.head.get_value()
        current = self.head.get_value()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            
            current = current.get_next()
        
        return max_value
        
