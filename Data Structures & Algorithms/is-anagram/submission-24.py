class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2={}
        if len(s) != len(t):
            return False 
        for i in s:
            hash1[i] = 1 + hash1.get(i,0)
        for j in t:
            hash2[j] = 1 + hash2.get(j,0)
        if  hash1 == hash2:
            return True
        else:
            return False
        