from queue import PriorityQueue

class Solution:
    def __init__(self):
        self.flights = {}   
        self.path = []
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            depart, arrival = ticket
            if depart not in self.flights:
                self.flights[depart] = PriorityQueue()
            self.flights[depart].put(arrival, arrival)  
        
        self.dfs("JFK")
        
        return self.path[::-1]
        
    def dfs(self, depart):
        
        arrivals = self.flights.get(depart)
        
        while arrivals and not arrivals.empty():
            self.dfs(arrivals.get())
        
        self.path.append(depart)