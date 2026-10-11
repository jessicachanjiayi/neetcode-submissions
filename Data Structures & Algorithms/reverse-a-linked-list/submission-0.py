# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteration
        prev, curr = None, head 

        while curr:
            temp = curr.next # Save the next node so we don't break the chain, this is the original node
            curr.next = prev # Reverse the Pointer
            prev = curr # Move prev to curr
            curr = temp # Move curr to temp
        return prev
