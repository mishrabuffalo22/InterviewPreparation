class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = [[x, y, z] for x, y, z in zip(startTime, endTime, profit)]
        arr.sort(key=lambda x: (-x[0], x[2]))
        maximums = [(arr[0][2], arr[0][0])]
        for start, end, profit in arr[1:]:
            if maximums[0][1] >= end:
                i = self.reverse_binary_search_right(maximums, end)
                if maximums[i - 1][0] + profit >= maximums[~0][0]:
                    maximums.append((maximums[i - 1][0] + profit, start))
            else:
                if maximums[~0][0] <= profit:
                    maximums.append((profit, start))
        return maximums[~0][0]
             
    @staticmethod
    def reverse_binary_search_right(two_dimensional, target):
        left, right = 0, len(two_dimensional)
        while left < right:
            middle = (left + right) // 2
            if two_dimensional[middle][1] > target - 1:
                left = middle + 1
            else:
                right = middle
        return left