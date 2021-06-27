# https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_vals = self.inorder(root, [])
        print(node_vals)
        return self.balance_util(node_vals, 0, len(node_vals)-1)
        
    
    def balance_util(self, node_vals, low, high):
        
        if low> high:
            return None
        
        mid = (low + high)//2
        
        root = TreeNode(node_vals[mid])
        root.left = self.balance_util(node_vals, low, mid-1)
        root.right = self.balance_util(node_vals, mid+1, high)
        
        return root
        
        
    
    def inorder(self, node, node_vals):
        if not node:
            return
        
        self.inorder(node.left, node_vals)
        node_vals.append(node.val)
        self.inorder(node.right, node_vals)
        
        return node_vals

        
