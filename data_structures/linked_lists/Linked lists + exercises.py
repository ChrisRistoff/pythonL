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
        while temp:
            print(temp.value)
            temp = temp.next


    def append_list(self, value):
        new_node = Node(value)

        if self.length == 0:
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

        if self.length== 0:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp


    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for i in range(index):
            temp = temp.next

        return temp


    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for i in range(index):
            temp = temp.next

        temp.value = value

        return True


    def insert(self, index, value):
        if index < 0 or index > self.length:
             return False

        if index == 0:
            return self.prepend_list(value)

        if index == self.length:
            return self.append_list(value)

        new_node = Node(value)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop_last()

        pre = self.get_value(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

#exercises

    def reverse(self):
        if self.length == 0:
             return None

        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        temp.next = None

        for i in range(self.length - 1):
            before = temp
            temp = after
            after = after.next
            temp.next = before

        return True


    def find_middle(self):
        n = 0
        temp = self.head
        while temp:
           temp = temp.next
           n += 1

        mid = self.head
        for i in range(n):
            if i % 2 == 1:
                mid = mid.next

        return mid

    def has_loop(self):
        temp1 = self.head
        temp2 = self.head

        while temp2 and temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next.next
            if temp1 == temp2:
                return True

        return False

    def remove_duplicates(self):
        if self.length == 0:
            return None

        current = self.head

        while current:
            temp = current

            while temp.next:
                if temp.next.value == current.value:
                    temp.next = temp.next.next
                    self.length -= 1

                else:
                    temp = temp.next

            current = current.next

        return True




my_linked_list = LinkedList(5)
my_linked_list.append_list(10)
my_linked_list.append_list(15)
my_linked_list.append_list(20)
my_linked_list.pop_last()
my_linked_list.prepend_list(1)
my_linked_list.prepend_list(2)
my_linked_list.pop_first()
print(my_linked_list.get_value(2))
my_linked_list.set_value(2, 100)
my_linked_list.insert(2, 50)
my_linked_list.remove(1)
my_linked_list.remove(0)




my_linked_list.append_list(50)
my_linked_list.append_list(10)
my_linked_list.append_list(10)
my_linked_list.remove_duplicates()

my_linked_list.print_list()
