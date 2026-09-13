class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)

        pos1 = []
        pos2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    pos1.append((i, j))

                if img2[i][j] == 1:
                    pos2.append((i, j))

        res = 0
        mp = {}

        for p1 in pos1:
            for p2 in pos2:
                r = p2[0] - p1[0]
                c = p2[1] - p1[1]

                key = (r, c)

                mp[key] = mp.get(key, 0) + 1

                res = max(res, mp[key])

        return res
        
