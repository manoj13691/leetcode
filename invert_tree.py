# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        a = deque()
        a.append(root)
        
        while a:
            cur_node = a.popleft()
            if cur_node is not None:
                # swap left and right children
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                a.append(cur_node.left)
                a.append(cur_node.right)
        return root
                
        
        
        
        