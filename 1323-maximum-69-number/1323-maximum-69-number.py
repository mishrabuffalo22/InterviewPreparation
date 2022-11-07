class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        l = list(num_str)
        for i in range(len(l)):
            if l[i]=='6':
                l[i]='9'
                break
        return int(''.join(l))
        