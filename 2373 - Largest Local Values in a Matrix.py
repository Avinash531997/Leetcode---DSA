class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)-2
        res=[]
        for i in range(0,n):
            row=[]
            for j in range(0,n):
                row.append(max(max(grid[i][j:j+3]), max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3])))
            res.append(row)
        return res


        
