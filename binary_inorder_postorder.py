# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder_index = len(postorder)-1
        inorder_element_index = {element:index for index, element in enumerate(inorder)}
        
        def helper(low, high):
            if low>high:
                return None
            
            cur_node_val = postorder[self.postorder_index]
            self.postorder_index -=1 
            pivot = inorder_element_index[cur_node_val]
            
            
            root = TreeNode(cur_node_val)
            root.right = helper(pivot+1, high)
            root.left = helper(low, pivot-1)
            
            return root
        
        return helper(0, len(postorder)-1)
         
        
        