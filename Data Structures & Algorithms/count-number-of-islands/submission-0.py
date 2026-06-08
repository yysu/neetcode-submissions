from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    number_of_island += 1
        return number_of_island
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            for (delta_x, delta_y) in directions:
                next_x, next_y = x + delta_x, y + delta_y
                if self.is_valid(next_x, next_y, grid, visited):
                    queue.append((next_x, next_y))
            
    def is_valid(self, x, y, grid, visited):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
            return True
        return False


        
        
        