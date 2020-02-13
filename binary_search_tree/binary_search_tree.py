import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value:
            if target == self.value:
                return True
            elif target < self.value and self.left:
                return self.left.contains(target)
            elif target > self.value and self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        max = self.value
        node = self
        while node.right:
            max = node.right.value
            node = node.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if(node.left):
            self.in_order_print(node.left)
        print(node.value)
        if(node.right):
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node:
            queue = Queue()
            queue.enqueue(node)
        while queue.len():
            current = queue.dequeue()
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            print(current.value)

        # visit node print value
        # add left to queue
        # add right to queue
        # remove current node from queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node:
            stack = Stack()
            stack.push(node)
        while stack.len():
            current = stack.pop()
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
