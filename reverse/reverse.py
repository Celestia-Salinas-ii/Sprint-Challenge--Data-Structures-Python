class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node=None, prev=None):
        if not self.head:
            return None
        if not prev:
            prev = LinkedList()
        if not node:
            node = self.head
        prev.add_to_head(node.value)
        if node.next_node:
            self.reverse_list(node.next_node, prev)
        if node == self.head and prev.head != None:
            self.head = prev.head
        return self