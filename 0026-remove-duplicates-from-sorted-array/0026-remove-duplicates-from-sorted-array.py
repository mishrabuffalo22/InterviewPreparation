class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        k=0
        i=0
        while i < len(a):
            f=i+1
            while f<len(a) and a[i]==a[f]:
                f=f+1
            a[k]=a[i]
            i=f
            k=k+1
        return k
            