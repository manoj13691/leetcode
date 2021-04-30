# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root==None:
            return None
        
        if root.val == p.val or root.val==q.val:
            return root
        left_sub = self.lowestCommonAncestor(root.left, p, q)
        right_sub = self.lowestCommonAncestor(root.right, p, q)
        
        if left_sub and right_sub:
            return root
        
        if left_sub:
            return left_sub
        
        return right_sub
        