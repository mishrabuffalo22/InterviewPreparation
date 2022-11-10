class Solution:
    def removeDuplicates(self, s: str) -> str:
        q = [s[0]]
        i=1
        while i<len(s):
            if q and s[i]==q[-1]:
                q.pop(-1)
            else:
                q.append(s[i])
            i+=1
        return ''.join(q)
        