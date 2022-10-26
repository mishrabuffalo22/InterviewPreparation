class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={}
        d[0]=-1
        if len(nums)<2:
            return 0
        for i in range(1,len(nums)):
            nums[i] = nums[i]+nums[i-1]
        for i in range(len(nums)):
            if nums[i]%k in d:
                if i-d[nums[i]%k]>=2:
                    return 1
            else:
                d[nums[i]%k] = i
        return 0
        