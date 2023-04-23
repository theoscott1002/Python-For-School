# ---------Deleting any Node by value in a linkedlist -----####

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

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

        return

    def delete_node(self, x):
        if self.head is None:
            print("No Node available")
            return
        if x == self.head.data:
            self.head = self.head.next
            return

        while x == self.head.next is not None:
            if x == self.head.next.data:
                break
            self.head = self.head.next
        if self.head.next is None:
            print("Node is not present")
        else:
            self.head.next = self.head.next.next


def main():
    myList = Linkedlist(6)
    myList.insert_at_end(10)
    myList.insert_at_end(15)
    myList.insert_at_end(20)
    myList.delete_node(4)
    myList.delete_node(5)
    print("here", myList.head.next.data)


main()
