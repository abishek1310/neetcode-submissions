class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght  = 0
        l = 0
        string = set()
        for r in  range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l = l+1  
            string.add(s[r])
            max_lenght = max(max_lenght, (r - l + 1 ))
        return max_lenght 
