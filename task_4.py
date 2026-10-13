class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.elem_count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.elem_count += 1

    def pop(self):
        if self.top is None:
            raise IndexError
        value = self.top.value
        self.top = self.top.next
        self.elem_count -= 1
        return value

    def peek(self):
        if self.top is None:
            raise IndexError
        return self.top.value

    def is_empty(self):
        return self.top is None