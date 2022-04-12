class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = list(str(n))
        
        for i in range(len(num) - 1, 0,-1):
            if num[i] < num[i - 1]:
                num[i - 1] = str(int(num[i - 1]) - 1)
                num[i] = "9"
                
                
        for j in range(1, len(num)):
            if num[j - 1] == "9":
                num[j] = "9"
                
        return int("".join(num))  
            
        
        