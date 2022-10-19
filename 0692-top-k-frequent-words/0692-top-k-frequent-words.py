
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d = dict(sorted(d.items(), key=lambda x:(-x[1],x[0])))
        d=list(d.keys())
        c=0
        l=[]
        k=k-1
        while k>=0:
            l.append(d[c])
            k-=1
            c+=1
        return l
        
        