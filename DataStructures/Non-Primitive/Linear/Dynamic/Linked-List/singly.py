class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Singly:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List \\ O(n)
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse Singly Linked List \\ O(n)
    def traverseList(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search for a node in Singly Linked List \\ O(n)
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The node does not exist in this SLL"

    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire SLL \\ O(1)
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = Singly()

singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 4)

print([node.value for node in singlyLinkedList])


singlyLinkedList.traverseSLL()


print(singlyLinkedList.searchSLL(33))
print(singlyLinkedList.searchSLL(3))


singlyLinkedList.deleteNode(0)
print([node.value for node in singlyLinkedList])


singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
