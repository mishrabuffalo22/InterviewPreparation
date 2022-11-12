import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        else:
            if -self.max_heap[0] < num:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            if len(self.max_heap) > len(self.min_heap)+1:
                p = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -p)
            elif len(self.min_heap) > len(self.max_heap):
                p = heapq.heappop(self.min_heap)
                print(p,2)
                heapq.heappush(self.max_heap, -p)
                
        

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            
            return (self.min_heap[0] + -self.max_heap[0])/2
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()