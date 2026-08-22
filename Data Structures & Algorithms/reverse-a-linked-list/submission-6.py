# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, current = None, head 

        while current:
            temp = current.next  #sets temp to the next value
            current.next = prev   #says the next value is the previous, stored above 
            prev = current   #preparing for the next iteration
            current = temp   #preparing for the next iteration 
        return prev
        