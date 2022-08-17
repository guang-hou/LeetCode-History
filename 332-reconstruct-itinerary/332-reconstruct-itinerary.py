class Solution:      
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            #targets[a].append(b)  # targets[a] = {e, d, c, b}  里面会倒序排列  
            targets[a] += [b]
            
        path = []

        def visit(start):
            dests = targets[start]
            while dests:
                smallestChild = dests.pop()
                visit(smallestChild)
            path.append(start)  # targets[start] now is empty, we are stuck, no further move unless go back one level up

        visit('JFK')
        return path[::-1]