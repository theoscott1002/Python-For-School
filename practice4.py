# ---------Adding elements at the end of a Linkedlist -------####

class Node:
    def __init__(self, data=None, prev=None):
        self.data = data
        self.prev = prev


class Linkedlist:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def insert_at_begin(self, data):
        newNode = Node(data)
        self.head.prev = newNode
        self.head = newNode
        self.length += 1


def main():
    myList = Linkedlist(12)
    myList.insert_at_begin(22)
    myList.insert_at_begin(30)
    print("here", myList.tail.prev.data)


main()
