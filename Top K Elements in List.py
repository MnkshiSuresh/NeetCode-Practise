class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        common=frequency.most_common(k)
        result = [elem for elem, _ in common]
        
        return result
        
        
