#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder_index=0
        inorder_element_index = {element:index for index, element in enumerate(inorder)}
        
        def helper(low, high):
            if low > high:
                return None
            
            cur_val = preorder[self.preorder_index]
            self.preorder_index +=1
            
            pivot = inorder_element_index[cur_val]
            root = TreeNode(cur_val)
            
            root.left = helper(low, pivot-1)
            root.right = helper(pivot+1, high)
            
            return root
        
        return helper(0, len(inorder)-1)
        
        
        