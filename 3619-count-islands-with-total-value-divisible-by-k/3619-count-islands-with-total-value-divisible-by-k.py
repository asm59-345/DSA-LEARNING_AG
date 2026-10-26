class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        visited = [[False] * n for _ in range(m)]
        island_count = 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    current_sum = 0
                    queue = [(i, j)]
                    visited[i][j] = True

                    idx = 0
                    while idx < len(queue):
                        r, c = queue[idx]
                        idx += 1
                        current_sum += grid[r][c]
                        
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] > 0:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                    
                    if current_sum % k == 0:
                        island_count += 1
                        
        return island_count