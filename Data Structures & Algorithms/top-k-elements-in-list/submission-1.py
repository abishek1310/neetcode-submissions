class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for  i in nums:
            dict[i]=1+ dict.get(i,0)
        l1=[]
        for i, j in dict.items():
            l1.append([j,i])
        l1.sort()
        l2=[]
        while(len(l2)<k):
            l2.append(l1.pop()[1])
        return l2 

        