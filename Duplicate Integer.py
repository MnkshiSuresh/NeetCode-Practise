class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        b=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i] in b:
                return True
            else:
                b.append(nums[i])
        return False

         
