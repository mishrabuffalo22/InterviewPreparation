class Solution:
    def calc(self, cur,nei):
        s=0
        for i in range(8):
            if cur[i]!=nei[i]:
                s+=1
        return s==1
    def minMutation(self, s: str, e: str, b: List[str]) -> int:
        q=[]
        d = {}
        for i in b:
            if i not in d:
                d[i]=0
        if e not in d:
            return -1
        q.append(s)
        count = 0
        vis = set()
        while q:
            n = len(q)
            for i in range(n):
                t = q.pop(0)
                if t==e:
                    print(t,e)
                    return count
                if t not in vis:
                    vis.add(t)
                    for j in b:
                        if self.calc(t,j):
                            q.append(j)
                                     
            count += 1
        return -1
            
                    
                
            
        
        