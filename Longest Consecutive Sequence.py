 def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        set(nums)
        array =[]
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            else:
                continue
            array.append(count)
        count=0
        return max(array)
