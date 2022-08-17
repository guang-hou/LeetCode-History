class Solution:      
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for dept, dest in sorted(tickets)[::-1]:
            targets[dept].append(dest)         # targets["ATL"] = ["AAA", "ABB", "BBB"] 
                                         # {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}
        path, stack = [], ['JFK']

        while stack:
            while targets[stack[-1]]:
                largestChild = targets[stack[-1]].pop()
                stack.append(largestChild)  # add largets first to stack, which will be visited in the last

            path.append(stack.pop())

        return path[::-1]