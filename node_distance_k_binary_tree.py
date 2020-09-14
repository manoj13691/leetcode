# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Convert tree to graph and find path from a node(target) to nodes at distance K

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        self.buildGraph(root, None, graph)
        
        res = []
        seen = set()
        queue = deque()
        queue.append((target.val, 0))
        seen.add(target.val)
        
        while queue:
            #print(queue)
            node_val, dist = queue.popleft()
            if dist==K:
                res.append(node_val)
                
            for neighbor in graph[node_val]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, dist+1))
        
        return(res)
        
    
    def buildGraph(self, node, parent, graph):  
        if node is None:
            return
        
        if parent is not None: # build an edge from cur_node to its parent
            graph[node.val].append(parent.val)
        
        # build an edge from node (parent) to its left and right child
        if node.left:
            graph[node.val].append(node.left.val)
            self.buildGraph(node.left, node, graph)
        
        if node.right:
            graph[node.val].append(node.right.val)
            self.buildGraph(node.right, node, graph)
            
            
        return 
