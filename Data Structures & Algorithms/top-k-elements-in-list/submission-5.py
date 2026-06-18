class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            hash[nums[i]] = 1+ hash.get(nums[i],0)
        l1=[]
        for i,j in hash.items():
            l1.append([j,i])
        l1.sort()
        l2=[]
        while len(l2)<k:
            l2.append(l1.pop()[1])
        return l2
            
        