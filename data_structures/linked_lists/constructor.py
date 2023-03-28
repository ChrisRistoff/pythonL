class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append_list(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True


    def pop_last(self):
        if self.length == 0:
            return None

        temp = self.head
        new_tail = temp

        while temp.next:
            new_tail = temp
            temp = temp.next

        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


    def prepend_list(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True




my_linked_list = LinkedList(5)
my_linked_list.append_list(10)
my_linked_list.append_list(15)
my_linked_list.append_list(20)
my_linked_list.pop_last()
my_linked_list.prepend_list(1)


my_linked_list.print_list()



