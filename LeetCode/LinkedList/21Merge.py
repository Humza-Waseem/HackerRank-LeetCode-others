class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init(self):
        self.root = None

    def Insert(self,val):
        newNode = Node(val)
        if(self.root == None):
            self.root = newNode
            print("value Inserting at Root")

        else:
            current= self.root
            while(current.next != None):
                current = current.next

            current.next = newNode
            print("value Inserted")

    def Search(self, data):
        current.val = self.root.val
        while(current.val != data):
            current.next.val

        return current.val


LL = LinkedList()
LL.Insert(4)
LL.Insert(3)
LL.Insert(9)
LL.Search(2)





