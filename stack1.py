class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.length = 1

    def printStack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def getTop(self):
        if self.top is None:
            print("Top: null")
        else:
            print("Top: " + self.top.value)


def main():
    myStack = Stack(20)
    myStack.getTop(5)
    myStack.printStack()


main()
