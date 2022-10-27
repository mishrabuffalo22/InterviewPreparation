class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        r = len(img1)
        c = len(img1[0])
        d={}
        l = []
        for i in range(r):
            for j in range(c):
                if img2[i][j]==1:
                    l.append([i,j])
        
        for i in range(r):
            for j in range(c):
                if img1[i][j]==1:
                    for k in l:
                        f = (k[0]-i,k[1]-j)
                        if f in d:
                            d[f]+=1
                        else:
                            d[f] = 1
        m=0
        g=-1
        for key,val in d.items():
            if val>m:
                m=val
                g=key

        return m
                
                
                
        
        