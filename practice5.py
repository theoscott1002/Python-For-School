# -------Adding element before a given Node in a Linkedlist ------#####

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
            self.length += 1
        return self

    def add_before(self, data, x):
        while self.head.next is not None:
            if self.head.next.data == x:
                break
            self.head = self.head.next
        #if self.head.next is None:
            #print("Node not found")

        else:
            newNode = Node(data)
            newNode.next = self.head.next
            self.head.prev = newNode
            self.length += 1

        return self


def main():
    myList = Linkedlist(10)
    print('here', myList.head.data)


main()
