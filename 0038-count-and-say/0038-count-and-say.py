class Solution:
    def solve(self, n):
        if n==1:
            return "1"
        s = self.solve(n-1)
        c=1
        p=''
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c+=1
            else:
                p=p+str(c)+s[i-1]
                c=1
        p=p+str(c)+s[len(s)-1]
        
        return p
        
    def countAndSay(self, n: int) -> str:
        return self.solve(n)
        
        