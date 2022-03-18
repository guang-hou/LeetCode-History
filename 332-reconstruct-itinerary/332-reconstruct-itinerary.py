class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        combined_tickets = defaultdict(list)
        
        for start, end in tickets:
            combined_tickets[start].append(end)
        
        for start, ends in combined_tickets.items():
            ends.sort()
        
        path, res = ["JFK"], []
        
        def backtrack(start):
            if len(path) == len(tickets) + 1:
                res.append(path[:])
                return
            
            if res:
                return
            
            # if start not in combined_tickets:
            #     return
            
            ends = combined_tickets[start]
            for i in range(len(ends)):
                end = ends[i]
                path.append(end)
                ends.pop(i)
                backtrack(end)
                ends.insert(i, end)
                path.pop()
        
        backtrack("JFK")
        
        return res[0]