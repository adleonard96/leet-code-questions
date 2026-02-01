class RecentCounter:

    def __init__(self):
        self.starting_pos = 0
        self.pings = []
        self.res_per_ping = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        
        min_val = t - 3000

        while self.pings[self.starting_pos] < min_val:
            self.starting_pos += 1
        
        return len(self.pings) - self.starting_pos


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)