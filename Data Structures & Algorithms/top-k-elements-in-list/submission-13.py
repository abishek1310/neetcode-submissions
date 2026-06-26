class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        list1= []
        for i, j in count.items():
            list1.append([j,i])
        list1.sort()
        list2=[]
        while len(list2)<k:
            list2.append(list1.pop()[1]) 
        return list2 
        