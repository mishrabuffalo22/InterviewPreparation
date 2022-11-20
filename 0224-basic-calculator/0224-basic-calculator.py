class Solution:
    def calculate(self, s: str) -> int:
        l= []
        sum = 0
        sign = 1
        i=0
        while i < len(s):
            j=i
            num = 0
            while j<len(s) and s[j]>='0' and s[j]<='9':
                num = num*10+int(s[j])
                j+=1
            i=j
            sum += num*sign
            if i<len(s) and s[i]==' ':
                i+=1
                continue
            elif i<len(s) and s[i]=='+':
                sign = 1
                i+=1
            elif i<len(s) and s[i]=='-':
                sign = -1
                i+=1
            elif i<len(s) and s[i]=='(':
                l.append(sum)
                l.append(sign)
                sum = 0
                sign = 1
                i+=1
            elif i<len(s) and s[i]==')':
                a = l.pop(-1)*sum + l.pop(-1)
                sum = a
                i+=1
        return sum
                
            
            
                
                
        