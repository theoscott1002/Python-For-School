class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


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
            self.head.next = self.head
            self.head = newNode
            self.length += 1
        return self


def main():
    myList = Linkedlist(12)
    myList.insert_at_begin(22)
    myList.insert_at_begin(30)
    print("here", myList.head.data)
    print(myList.tail.data)


main()
