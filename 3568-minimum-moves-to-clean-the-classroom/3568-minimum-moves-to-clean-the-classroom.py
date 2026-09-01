class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m,n = len(classroom),len(classroom[0])
        start_r , start_c = -1,-1
        litter_map = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_r , start_c = r, c
                elif cell == 'L':
                    litter_map[( r, c )] = litter_count
                    litter_count += 1
        target_mask = (1 << litter_count) -1 

        best_energy = [[[-1] * (1 << litter_count) for _ in range(n) ] for _ in range(m) ]

        queue = deque([(start_r, start_c , 0 , energy , 0)])

        best_energy[start_r][start_c][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r ,c , mask , cur_e , steps = queue.popleft()

            if mask == target_mask:
                return steps
            if cur_e == 0:
                continue

            for dr, dc in directions:
                nr , nc = r + dr , c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = cur_e - 1
                    next_mask = mask
                    cell = classroom[nr][nc]
                    
                    if cell == 'R':
                        next_e = energy
                    
                    elif cell == 'L':
                        l_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << l_idx)
                    
                    if next_e > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1

        