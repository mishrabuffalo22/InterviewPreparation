# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        q = p
        p=p.next
        
        while p is not None:
            p.val,q.val=q.val,p.val
            p=p.next
            if p is None:
                q.next=None
                break
            q=q.next
            
        