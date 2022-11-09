class StockSpanner:

    def __init__(self):
        self.q = [[10**9,-1]]
        self.i = -1

    def next(self, price: int) -> int:
        self.i += 1
        while self.q and price>=self.q[-1][0]:
            self.q.pop(-1)
        r=None
        r = self.i-self.q[-1][1]
        self.q.append([price,self.i])
        return r
        
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)