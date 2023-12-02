# function to reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # while(head):
        #     nextNode = head.next
        #     head.next = prev
        #     prev = head
        #     head = nextNode
        # head = prev   
        # return head


        prev = None
        # while(head):
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
        current = prev   
        return reverseList(current)
        




    


# Runtime 34ms
# Beats 94.28% of users with Python3