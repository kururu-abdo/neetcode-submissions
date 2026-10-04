class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid) , len(grid[0])

        def explore(r , c):

           if r < 0 or r >= rows  or c < 0 or c >= cols or grid[r][c] != '1':
              return
           grid[r][c]= '0' 
           explore(r + 1, c)
           explore(r- 1, c)
           explore(r, c + 1)
           explore(r, c- 1)
        islands= 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== '1':
                  islands += 1
                  explore(r, c)

        return islands
