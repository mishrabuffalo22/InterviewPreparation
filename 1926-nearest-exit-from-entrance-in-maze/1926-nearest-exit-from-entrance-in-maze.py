class Solution:

    def is_valid(self, x,y, m,n):
        if x<m and y<n and x>=0 and y>=0:
            return 1
        return 0

    def nearestExit(self, maze: List[List[str]], ent: List[int]) -> int:
        q = [ent]
        m = len(maze)
        n = len(maze[0])
        # d = {}
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or i==m-1 or j==0 or j==n-1:
        #             if (i,j) != (ent[0],ent[1]) and maze[i][j] != '+':
        #                 d[(i,j)] = 1
        # if not d:
        #     return -1
        count = 0
        maze[ent[0]][ent[1]] = 1
        while q:
            d = len(q)
            for i in range(d):
                p = q.pop(0)
                if (0 in [p[0],p[1]] or p[0]==m-1 or p[1]==n-1) and [p[0],p[1]] != ent:
                    return count
                #right
                if self.is_valid(p[0]+1,p[1], m,n) and maze[p[0]+1][p[1]] =='.':
                    q.append([p[0]+1,p[1]])
                    maze[p[0]+1][p[1]] = 1
                #down
                if self.is_valid(p[0],p[1]+1, m,n) and maze[p[0]][p[1]+1] =='.':
                    q.append([p[0],p[1]+1])
                    maze[p[0]][p[1]+1] = 1
                #left
                if self.is_valid(p[0]-1,p[1], m,n) and maze[p[0]-1][p[1]] =='.':
                    q.append([p[0]-1,p[1]])
                    maze[p[0]-1][p[1]] = 1
                #up
                if self.is_valid(p[0],p[1]-1, m,n) and maze[p[0]][p[1]-1] == '.':
                    q.append([p[0],p[1]-1])
                    maze[p[0]][p[1]-1] = 1
            count += 1
        return -1
                    
                
        