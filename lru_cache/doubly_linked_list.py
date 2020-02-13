"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if not self.head:
            return 'Empty'
        else:
            nodes = []
            node = self.head
            while node:
                values = {'value': node.value}
                if node.prev:
                    values['prev'] = node.prev.value
                else:
                    values['prev'] = None
                if node.next:
                    values['next'] = node.next.value
                else:
                    values['next'] = None
                if self.tail == node:
                    values['tail'] = True
                if self.head == node:
                    values['head'] = True
                nodes.append(values)
                node = node.next
            return f'{nodes}'
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head:
            self.head = ListNode(value, None, self.head)
            self.head.next.prev = self.head
        else:
            self.head = ListNode(value, None, None)
            self.tail = self.head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = None
        if not self.head:
            return value
        elif self.head.next:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
        else:
            value = self.head.value
            self.head = None
            self.tail = None
        self.length -= 1
        return value
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.tail:
            self.tail.next = ListNode(value, self.tail, None)
            self.tail = self.tail.next
        else:
            self.head = ListNode(value, None, None)
            self.tail = self.head
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = None
        if not self.tail:
            return value
        if self.tail and self.tail.prev:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            value = self.tail.value
            self.tail = None
            self.head = None
        self.length -= 1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node and self.head and node != self.head:
            if(node == self.tail):
                self.tail = node.prev
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.next = self.head
            node.next.prev = node
            node.prev = None
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node and self.head and node != self.tail:
            if self.head == node:
                self.head = self.head.next
                self.head.prev = None
            if node.prev:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node and self.head:
            if node == self.head and node == self.tail:
                self.head = None
                self.tail = None
            elif node == self.head:
                self.head = node.next
            elif node == self.tail:
                self.tail = node.prev

            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None
        else:
            node = self.head
            max = node.value
            while node.next:
                if node.next.value > max:
                    max = node.next.value
                node = node.next
            return max