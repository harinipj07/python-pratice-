class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        startwith = [0]*26
        for c in s[::-1]:
            startwith[ord(c)-ord('a')] = sum(startwith) + 1
        return sum(startwith)%(10**9+7)

        
