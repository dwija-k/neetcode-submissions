# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()  #make 2 'empty' linked lists 

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1  #make next node point to list1
                list1 = list1.next  #point to next node 
            else:
                node.next = list2
                list2 = list2.next 
            node = node.next  #point to the next node [empty] in the output linked list

        node.next = list1 or list2  #one list will be empty so return from the other

        return dummy.next            
