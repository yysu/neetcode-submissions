from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    self.bfs(grid, i, j, visited)
                    ans += 1
        return ans
    
    def bfs(self, grid, i, j, visited):
        queue = deque([(i, j)])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue

            visited.add((x, y))
            for delta_x, delta_y in directions:
                new_x = x + delta_x
                new_y = y + delta_y
                if self.is_valid(new_x, new_y, grid, visited):
                    queue.append((new_x, new_y))
    
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
            return True
        return False
