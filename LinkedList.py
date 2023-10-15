# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def traverse(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next

# # Example usage:
# linked_list = LinkedList()
# linked_list.append('a')
# linked_list.append(1)
# linked_list.append('+')

# linked_list.traverse()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node('H')
b = Node('A')
c = Node('M')
d = Node('Z')
e = Node('A')


a.next = b
b.next = c
c.next = d
d.next = e

def PrintLinkedList(head):     # here the head can be any element from which we are starting the iteration
    current = head
    while current != None :

        print (current.data)
        current=current.next
        

PrintLinkedList(a)


