# https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.ans = 0
        self.dfs(root, targetSum)
        return self.ans
        
    
    def dfs(self, root, target):
        if root is None:
            return 
        
        self.dfs2(root,target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        
    
    def dfs2(self, node, target):
        if node is None:
            return
        
        if node.val==target:
            self.ans+=1
        
        self.dfs2(node.left, target-node.val)
        self.dfs2(node.right, target-node.val)
        
    
        