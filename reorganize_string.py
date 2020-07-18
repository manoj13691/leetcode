# https://leetcode.com/problems/reorganize-string/
# https://www.youtube.com/watch?v=zaM_GLLvysw

import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        #S = "BBBBaaa"
        char_count_tuple  = Counter(S).most_common()
        for char, count in char_count_tuple:
            heapq.heappush(heap, (-count, char))
        
        ans = ""
        heapq.heapify(heap)
        while len(heap)>1:
            temp_1 = heapq.heappop(heap)
            count_1, char_1 = -temp_1[0], temp_1[1]
            
            temp_2 = heapq.heappop(heap)
            count_2, char_2 = -temp_2[0], temp_2[1]
            
            #print(char, count)
            ans = ans + char_1+char_2
            count_1 = count_1 - 1
            count_2 = count_2 - 1
            
            if count_1 > 0:
                heapq.heappush(heap, (-count_1, char_1))
            if count_2 > 0:
                heapq.heappush(heap, (-count_2, char_2))
        
        # length of heap will be 1
        if len(heap)==1:
            temp = heapq.heappop(heap)
            count, char = -temp[0], temp[1]

            if count > 1:
                return ""

            else: # count will be 1. count will not be zero coz we wont add anything equal to zero in heap
                ans = ans + char
        
        return ans
       
        
       
