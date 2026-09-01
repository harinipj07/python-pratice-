class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        lumetarkon = (classroom, energy)
        m, n = len(classroom), len(classroom[0])
        Emax = energy
        start = None
        litters = []

        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litters.append((i, j))

        k = len(litters)
        if k == 0:
            return 0

        litter_index = {pos: idx for idx, pos in enumerate(litters)}
        full_mask = (1 << k) - 1
        best_e = [
            [ [-1] * (1<<k) for _ in range(n) ]
            for __ in range(m)
        ]

        sx, sy = start
        init_mask = 0
        best_e[sx][sy][init_mask] = Emax
        dq = deque([ (sx, sy, init_mask, 0) ])  
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while dq:
            x, y, mask, moves = dq.popleft()
            curr_e = best_e[x][y][mask]
            if mask == full_mask:
                return moves

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                cell = classroom[nx][ny]
                if cell == 'X':
                    continue

                ne = curr_e - 1
                if ne < 0:
                    continue

                if cell == 'R':
                    ne = Emax

                nmask = mask
                if cell == 'L':
                    nmask |= 1 << litter_index[(nx, ny)]

                if ne <= best_e[nx][ny][nmask]:
                    continue
                best_e[nx][ny][nmask] = ne
                dq.append((nx, ny, nmask, moves+1))

        return -1
        
