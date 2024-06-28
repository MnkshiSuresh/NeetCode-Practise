class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output =[]
        for i in range(0,len(nums)):
            mul=1
            for j in range(0,len(nums)):
                if j==i:
                    continue
                else:
                    mul=mul*nums[j]
            output.append(mul)
        return output

        
