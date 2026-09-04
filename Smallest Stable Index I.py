class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        mn = [0] * n
                
        mn[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            mn[i] = min(nums[i], mn[i + 1])
                   
        mx = nums[0]
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn[i] <= k:
                return i
                
        return -1
        
