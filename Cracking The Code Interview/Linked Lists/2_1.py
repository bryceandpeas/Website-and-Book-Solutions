'''

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

'''

class Node(object):


    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next


    def __str__(self):
        return str(self.cargo)


    def get_cargo(self):
        return self.cargo


    def next_node(self, node):
        self.next = node


    def get_node(self):
        return self.next


class LinkedList(object):


    def __init__(self, input_list):
        assert len(input_list) > 0
        self.head = Node(input_list[0])
        iter_node = self.head

        for i in range(1, len(input_list)):
            iter_node.next_node(Node(input_list[i]))
            iter_node = iter_node.get_node()
        iter_node.next_node(None)


    def remove_duplicates(self):
        assert self.head is not None
        anchor = self.head

        while anchor is not None:
            iterator = anchor
            while iterator is not None:
                prev = iterator
                iterator = iterator.get_node()

                if iterator is None:
                    break

                if iterator.get_cargo() == anchor.get_cargo():
                    next = iterator.get_node()
                    prev.next_node(next)

            anchor = anchor.get_node()


    def __str__(self):
        iter_node = self.head
        linked_out = []

        while iter_node is not None:
            linked_out.append(iter_node.get_cargo())
            iter_node = iter_node.get_node()

        return str(linked_out)
