# function to reverse Linked List
# Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # prev = None
#         # while(head):
#         #     nextNode = head.next
#         #     head.next = prev
#         #     prev = head
#         #     head = nextNode
#         # head = prev   
#         # return head


#         prev = None
#         # while(head):
#         nextNode = current.next
#         current.next = prev
#         prev = current
#         current = nextNode
#         current = prev   
#         return reverseList(current)


import time 
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, it is already sorted. That is the time to stop recursive call as the base case     is reached
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively divide each half into halves until you reach the base case which is a list with 0 or 1 elements
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves back together
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left and right lists (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result
        
# Example usage:
# start = time.time()
# my_array = [38, 27, 43, 3, 9, 82, 10]
# end = time.time()
# TOTALTIME = end- start
# # merge_sort(my_array)
# print(TOTALTIME)
# print("Sorted array:",merge_sort(my_array))

        




    


# Runtime 34ms
# Beats 94.28% of users with Python3






def reversedWords(sentence):
    stack = []
    tempWord = ""

     
    for i in range(0,len(sentence) ):
        if(sentence[i] != ' '):
            tempWord = tempWord + sentence[i]
        else:
            stack.append(tempWord)
            tempWord = ""

    stack.append(tempWord)

    reversedSentence = ""

    while stack:
        reversedSentence += stack.pop() + ' '

    return reversedSentence  
    

    

    # print(stack)



sentence = "I am from University of Engineering and Technology Lahore" # we pop from Lahore to I   
          # 9<-8 <-7    <-6      <-5   <-4      <-3   <- 2   <-   1
output_sentence = reversedWords(sentence)

print(output_sentence)