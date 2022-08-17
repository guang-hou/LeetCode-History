class Solution:      
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for dept, dest in sorted(tickets)[::-1]:
            targets[dept].append(dest)         # targets["ATL"] = ["AAA", "ABB", "BBB"] 
                                         # {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}

        path, stack = [], ['JFK']

        while stack:
            # add all child nodes to stack
            if targets[stack[-1]]:
                while targets[stack[-1]]:
                    largestChild = targets[stack[-1]].pop()  #### here dests will not affect targets
                    stack.append(largestChild)  # add largets first to stack, which will be visited in the last
            else:
                dest = stack.pop()
                path.append(dest)

        return path[::-1]