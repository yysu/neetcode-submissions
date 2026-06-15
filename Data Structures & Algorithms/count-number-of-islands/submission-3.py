from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nums = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    nums += 1
                    self.bfs(grid, i, j, visited)
        return nums
    
    def bfs(self, grid, i, j, visited):
        queue = deque([(i, j)])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            for delta_x, delta_y in directions:
                new_x, new_y = x + delta_x, y + delta_y
                if self.is_valid(grid, new_x, new_y, visited):
                    queue.append((new_x, new_y))
    
    def is_valid(self, grid, x, y, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
            return True
        return False
                