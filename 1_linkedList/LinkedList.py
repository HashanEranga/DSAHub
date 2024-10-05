from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, value):
        # 1: create a new node
        new_node = Node(value)

        # 2: assign next pointer of the new node to head
        new_node.next = self.head

        # 3: set new_node as the new head
        self.head = new_node

    def get_head_value(self):
        if self.head is not None:
            return self.head.value
        else:
            return -1
