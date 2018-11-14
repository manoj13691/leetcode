# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
# Time Limit exceeded error

def kthSmallest( matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import sys
        k_indices =[0] * len(matrix[0])
        
        count = 0
        min_val = sys.maxsize
        global_min = sys.maxsize
        min_val_index = -1

        while(count < k):
            for i in range(len(k_indices)):
                if k_indices[i] < len(matrix[0]):
                    if matrix[i][k_indices[i]] < min_val:
                        min_val = matrix[i][k_indices[i]]
                        min_index = i
            k_indices[min_index] +=1
            global_min = min_val
            min_val = sys.maxsize
            count+=1
        print(global_min)

kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)

