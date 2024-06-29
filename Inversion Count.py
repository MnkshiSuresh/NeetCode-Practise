from typing import List

class Solution:
    def getInversionCount(self, array: List[int]) -> int:
        a = []
        for i in range(0, len(array)):
            for j in range(i + 1, len(array)):
                if array[i] > array[j]:
                    a.append((array[i], array[j]))
        return len(a)

                
        
            

	

		


