# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math  
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        middle = 0
        vals = []
        while head != None:
            size += 1
            vals.append(head)
            head = head.next
        middle = math.floor(size/2)
        return vals[middle]

#OPTIMIZED 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math  
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head
        while(end != None and end.next != None):
            end = end.next.next
            middle = middle.next
        return middle
        