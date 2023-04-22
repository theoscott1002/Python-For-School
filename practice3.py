# ------Adding element at the end of a Linkedlist ---------###3

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

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
    myList = LinkedList(5)
    myList.insert_at_end(10)
    myList.insert_at_end(15)
    myList.insert_at_end(20)

    print('here', myList.head.data)


main()
