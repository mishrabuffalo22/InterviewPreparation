class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        f = l[::-1]
        return ' '.join(f)
        
                
        
        