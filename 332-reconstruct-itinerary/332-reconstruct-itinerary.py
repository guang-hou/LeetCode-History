from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # get depts -> dests (with dests in reverse sorted order, since we're popping)
        dept_to_dests = defaultdict(list)
        for dept, dest in sorted(tickets, reverse=True):
            dept_to_dests[dept].append(dest)

        route = []
        stack = ['JFK']

        while stack:
            while dept_to_dests[stack[-1]]:
                t_dest = dept_to_dests[stack[-1]].pop()
                stack.append(t_dest)

            route.append(stack.pop())

        return list(reversed(route))