class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_R, num_D = senate.count("R"), senate.count("D")
        need_skip_R, need_skip_D = 0, 0
        skipped_R, skipped_D = 0, 0
        skipped = []
        
        while need_skip_R < num_R and need_skip_D < num_D:
            for i, char in enumerate(senate):
                if i in skipped:
                    continue
                
                if char == "D":
                    if skipped_D < need_skip_D:
                        skipped_D += 1
                        skipped.append(i)
                        continue
                    else:
                        need_skip_R += 1
                        if need_skip_R == num_R:
                            break
                else:
                    if skipped_R < need_skip_R:
                        skipped_R += 1
                        skipped.append(i)
                        continue
                    else:
                        need_skip_D += 1
                        if need_skip_D == num_D:
                            break
                            
        if need_skip_R >= num_R:
            return "Dire"
        elif need_skip_D >= num_D:
            return "Radiant"