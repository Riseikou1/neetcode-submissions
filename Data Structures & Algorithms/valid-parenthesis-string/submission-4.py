class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        left = []
        for idx, char in enumerate(s) :
            if char == '(' :
                left.append(idx)
            elif char == '*' :
                star.append(idx)
            else :
                if not left :
                    if not star : return False
                    star.pop()
                else :
                    left.pop()
        
        while left and star :
            if left.pop() > star.pop() :
                return False

        return not left
