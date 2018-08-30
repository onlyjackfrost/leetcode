# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle = end = head
        while end.next and end.next.next :
            middle = middle.next
            end = end.next.next
        if end.next :
            middle = middle.next
        return middle
        