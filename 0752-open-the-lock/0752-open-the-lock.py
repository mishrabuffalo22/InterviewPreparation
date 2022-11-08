class Solution:
    def get_comb(self, l):
        f = []
        for i in range(4):
            g = l[:i]+str((int(l[i])+1)%10)+l[i+1:]
            f.append(g)
            h = l[:i]+str((int(l[i])-1)%10)+l[i+1:]
            f.append(h)
        return f
    def openLock(self, dead: List[str], target: str) -> int:
        d = set(dead)
        if target in d:
            return -1
        q = []
        q.append('0000')
        count = 0
        while q:
            for i in range(len(q)):
                l = q.pop(0)
                if l==target:
                    return count
                if l in d:
                    continue
                d.add(l)
                for j in self.get_comb(l):
                    q.append(j)
            count += 1
        return -1
            
        