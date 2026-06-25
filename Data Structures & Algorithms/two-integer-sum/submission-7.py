class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i, v in enumerate(nums):
            key = target - v 
            if key in hash:
                return [hash[key], i]
            else:
                hash[v] = i
        return 
        