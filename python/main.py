class Node:
    def __init__(self,value):
        self.value=value
        self.next= None


class LinkedList:
    def __init__(self):
      self.head=None
      self.tail=None
      self.length=0
    def push(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
           self.tail.next = newNode
           self.tail = newNode
        self.length += 1
        print(self)

    def getValues(self):
        temp = self.head
        while temp:
            print(temp.value, end="-->")
            temp = temp.next
       

l = LinkedList()

l.push(0)
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.getValues()
