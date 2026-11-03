import heapq
from math import isqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-g for g in gifts]   
        heapq.heapify(heap)          

        for _ in range(k):
            top = -heapq.heappop(heap)          
            heapq.heappush(heap, -isqrt(top))   

        return -sum(heap)