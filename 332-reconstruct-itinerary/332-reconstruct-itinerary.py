class Solution:
    def __init__(self):
        self.departArrivalCounts = defaultdict(dict)   
        self.path = ["JFK"]
        self.res = []
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            depart, arrival = ticket
            allArrivals = self.departArrivalCounts[depart]
            allArrivals[arrival] = allArrivals.get(arrival, 0) + 1
        
        for depart, arrivals in self.departArrivalCounts.items():
            self.departArrivalCounts[depart] = dict(sorted(arrivals.items()))
        
        targetLength = len(tickets) + 1
        
        self.dfs("JFK", targetLength)
        
        return self.res[0]
        
    def dfs(self, depart, targetLength):
        
        if len(self.path) == targetLength:
            self.res.append(self.path[:])
            return
        
        if self.res:
            return
        
        allArrivals = self.departArrivalCounts[depart]
        
        for arrival in allArrivals:
            if allArrivals[arrival] > 0:
                allArrivals[arrival] -= 1
                self.path.append(arrival)
                self.dfs(arrival, targetLength)
                allArrivals[arrival] += 1
                self.path.pop()