# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def recur(self, root):
        if not root:
            return
        self.count+=1
        self.recur(root.left)
        self.recur(root.right)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.recur(root)
        return self.count
        
        