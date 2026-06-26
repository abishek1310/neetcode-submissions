class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        prefix = 1
        for i in range (len(nums)):
            l[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            l[j] = l[j]* postfix
            postfix = postfix * nums[j]
        return l

            
        