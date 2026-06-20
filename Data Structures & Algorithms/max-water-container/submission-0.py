class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_storage= 0 
        l=0
        r = len(heights)-1 
        while l<r:
            area = (r-l) * min(heights[l],heights[r])
            if area>max_storage:
                max_storage = area
            else:
                max_storage = max_storage
            
            if heights[l]<heights[r]:
                l += 1 
            else:
                r -= 1
        return max_storage