# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Iteration with 2 Pointers, Time O(n+m), Space O(1)
        dummy = node = ListNode() 

        while list1 and list2: # list1 and list2 both have data
            if list1.val < list2.val: # list1 has a smaller starting value
                node.next = list1 # Attach the smaller node to node.next
                list1 = list1.next # Move forward in the chosen list
            else:
                node.next = list2
                list2 = list2.next
            node = node.next # move node to node next
        node.next = list1 or list2 # only 1 list has data
        return dummy.next 