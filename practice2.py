class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Linkedlist:
    def __init__(self, value, value2, value3):
        newNode1 = Node(value)
        newNode2 = Node(value2)
        newNode3 = Node(value3)
        self.head = newNode1
        self.head.next = newNode2
        self.tail = newNode3
        self.length = 3

    def insert_at_end(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return self


def main():
    myList = Linkedlist(7, 8, 9)
    myList.insert_at_end(10)
    print('here', myList)


main()



