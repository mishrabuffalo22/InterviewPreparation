class Solution:
    def checkIfPangram(self, s: str) -> bool:
        l = [0]*26
        for i in s:
            l[ord(i)-ord('a')]+=1
        for i in l:
            if i==0:
                return 0
        return 1
        