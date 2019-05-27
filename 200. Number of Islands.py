from collections import deque

class Solution(object):
    
    def checkSurroundings(self, grid, queue):
        
        row = len(grid)
        column = len(grid[0])
        
        while queue:
            
            i, j = queue.pop()
            #print grid_piece, i, j
             
            if i + 1 < row:
                if grid[i+1][j] == '1':
                    grid[i+1][j] = '0'
                    queue.appendleft((i+1, j))
            if i-1 >=0 :
                if grid[i-1][j] == '1':
                    grid[i-1][j] = '0'
                    queue.appendleft((i-1,j))
            if j+1 <column:
                if grid[i][j+1] == '1':
                    grid[i][j+1] = '0'
                    queue.appendleft((i, j+1))
            
            if j-1 >= 0:
                if grid[i][j-1] == '1':
                    grid[i][j-1] = '0'
                    queue.appendleft((i, j-1))       
            
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if len(grid) == 0:
            return 0
        
        island_counter = 0
        queue = deque(list())
        row = len(grid)
        column = len(grid[0])
        
        for i in range(row):
            
            for j in range(column):
                
                grid_piece = grid[i][j]

                if grid_piece == '1':
                    island_counter += 1
                    grid[i][j] = '0'
                    queue.appendleft((i, j))
                    self.checkSurroundings(grid, queue)
            
        return island_counter
                    
    
                        
                