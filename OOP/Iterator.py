class ListNode:
    def __init__(self, value):
        self.head = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            value = self.current
            self.current = self.current.next
            return value

        raise StopIteration


if __name__ == '__main__':
    head = ListNode("o/")
    head.next = ListNode("eggs")
    head.next.next = ListNode("and")
    head.next.next.next = ListNode("spam")

    my_list = LinkedList(head)

    for node in my_list:
        print(node.head)
