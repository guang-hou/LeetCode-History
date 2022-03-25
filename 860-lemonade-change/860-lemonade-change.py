class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            elif bill == 20:
                twenty += 1
                if ten > 0:
                    ten -= 1
                    if five > 0:
                        five -= 1
                    else:
                        return False
                else:
                    if five >= 3:
                        five -= 3
                    else:
                        return False
            
        return True
            