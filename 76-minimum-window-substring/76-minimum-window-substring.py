class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)  # only track chars in t
        need = defaultdict(int)
        
        for c in t:
            need[c] += 1
        
        # need = Counter(t)

        left, right = 0, 0
        start, length = 0, float('inf')
        numOfMatchingChar = 0
        
        while right < len(s):
            # print(left, right)
            rightChar = s[right]
            right += 1
            
            if (rightChar in need):
                window[rightChar] += 1
                if (window[rightChar] == need[rightChar]):
                    numOfMatchingChar += 1
            
            while (numOfMatchingChar == len(need)):
                if (right - left < length):
                    start = left
                    length = right - left
                leftChar = s[left]
                left += 1
                if (leftChar in need):
                    if (window[leftChar] == need[leftChar]):
                        numOfMatchingChar -= 1
                    window[leftChar] -= 1
            
            
        return "" if length == float('inf') else s[start: start + length]
        
                