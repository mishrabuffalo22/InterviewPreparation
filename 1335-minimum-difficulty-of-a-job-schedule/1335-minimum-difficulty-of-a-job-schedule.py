class Solution:
    def solve(self, ind, d, job,dp):
        if d<0:
            return 10**9
        if d==1:
            ma=0
            for i in range(ind, len(job)):
                ma=max(ma,job[i])
            return ma
        if dp[ind][d] != -1:
            return dp[ind][d]
        mi = 10**9
        ma=0
        for i in range(ind,len(job)-d+1):
            ma=max(ma, job[i])
            mi = min(mi, ma+self.solve(i+1,d-1,job,dp))
        dp[ind][d]=mi
        return dp[ind][d]
            
    def minDifficulty(self, job: List[int], d: int) -> int:
        if d>len(job):
            return -1
        dp=[[-1 for i in range(d+1)] for j in range(len(job))]
        return self.solve(0,d,job,dp)
        
        