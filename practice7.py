# -------- Deleting at the end of a Linkedlist ----####

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
            return self

    def remove_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1

            if self.length == 0:
                self.head = None
                self.tail = None

            return temp


def main():
    myList = Linkedlist(10)
    myList.insert_at_end(15)
    myList.insert_at_end(20)
    myList.remove_at_end()
    print("here", myList.tail.data)


main()
