class Node:
    elem = 0
    next_node = None

    def __init__(self, elem: int, next_node=None):
        self.elem = elem
        self.next_node = next_node

    def swap_node(self):
        if self.next_node is not None:
            if self.elem > self.next_node.elem:
                t = self.next_node
                self.next_node = t.next_node
                t.next_node = self
                assert self.elem < t.next_node.elem
                return t
        return self


# Test Driver
if __name__ == '__main__':
    n = Node(1, Node(1))
    result = n.swap_node()
