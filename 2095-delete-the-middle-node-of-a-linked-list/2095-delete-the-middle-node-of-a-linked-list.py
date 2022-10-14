# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        s=head
        f=head
        q=ListNode()
        while f is not None and f.next!=None:
            f=f.next.next
            q=s
            s=s.next
        q.next=q.next.next
        return head
            
        