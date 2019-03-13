'''

Implement an algorithm to find the kth to last element of a singly linked list.

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


    def get_length(self):
        
        assert self.head is not None
        anchor = self.head
        input_length = 0

        while anchor is not None:
            iterator = anchor
            while iterator is not None:
                prev = iterator
                iterator = iterator.get_node()

                if iterator is None:
                    break

                if iterator.get_cargo() != None:
                    next = iterator.get_node()
                    prev.next_node(next)
                    input_length += 1

            anchor = anchor.get_node()
        return(input_length - 2)


    def find_from_last(self, k):
        assert self.head is not None
        anchor = self.head
        input_length = self.get_length()

        return(input_length)


input_list = ["hello", "world"]
linked_list = LinkedList(input_list)
print(linked_list.find_from_last(1))

