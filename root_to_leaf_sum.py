# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.util(root, 0)
        return self.util_2(root)
        
        
        
    def util(self, node, total_sum):
        if not node:
            return 0
        cur_val = total_sum*10 + node.val
        if not node.left and not node.right:
            return cur_val
        l = self.util(node.left, cur_val)
        r = self.util(node.right, cur_val)
        return l+r
    
    
    def util_2(self, node):
        queue = deque(root)
        
        while queue:
            cur_node, cur_sum = queue.popleft(), 0
            
            if cur_node.left is None and cur_node.right is None:
                cur_sum+= cur_node.val
                
            if cur_node.left:
                cur_node.left.val = cur_node.left.val + cur_node*10
                queue.append(cur_node.left)
            
            if cur_node.right:
                cur_node.right.val = cur_node.right.val + cur_node*10
                queue.append(cur_node.right)
            
        return cur_sum
                
                
            
            
    