class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Linkedlist:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def insert_at_begin(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.head.prev = newNode
            self.head = newNode
            self.length -= 1

        return self


def main():
    myList = Linkedlist(7)
    myList.insert_at_begin(33)
    myList.insert_at_begin(50)
    print('here', myList.tail.prev.data)


main()



