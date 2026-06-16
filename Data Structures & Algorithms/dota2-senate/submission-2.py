class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        count, i = 0, 0

        while i < len(senate) :
            char = senate[i]
            if char == 'R' :
                if count < 0 :
                    senate.append('D')
                count += 1
            else :
                if count > 0 :
                    senate.append('R')
                count -= 1
            i += 1

        return "Radiant" if count > 0 else "Dire"
