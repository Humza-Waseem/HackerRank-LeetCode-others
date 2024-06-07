# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.root = None

#     def PrintList(self):
#         current = self.root
#         while current is not None:
#             print(current.val)
#             current = current.next

#     def Insert(self, val):
#         newNode = Node(val)
#         if self.root is None:
#             self.root = newNode
#             print("value Inserting at Root")
#         else:
#             current = self.root
#             while current.next is not None:
#                 current = current.next
#             current.next = newNode
#             print("value Inserted")

#     def Search(self, data):
#       current = self.root
#       while current is not None:
#           if current.val == data:
#               return current
#           current = current.next
#       return None

#     def mergeList(self):



# list1= LinkedList()
# list2= LinkedList()
# list1.Insert(1)
# list1.Insert(2)
# list1.Insert(4)
# list2.Insert(1)
# list2.Insert(3)
# list2.Insert(4)

# # list1.PrintList()
# # list2.PrintList()


# print(mergeLists())






def  sqquare(x):
    if x == 0:
        return 0
    count = 0
    for  i in range(1,x):
        i = i * i 
        if( i <= x):
         count = count +1
    return count



x = 16
print(sqquare(x))