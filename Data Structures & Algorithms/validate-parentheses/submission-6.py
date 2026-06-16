class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        memo = {"}" : "{", "]" : "[",")" : "("}

        for char in s :
            if char in "([{" :
                stk.append(char)
            else :
                if not stk : return False
                if ((char == "}" and memo[char] != stk.pop()) or
                    (char == "]" and memo[char] != stk.pop()) or
                    (char == ")" and memo[char] != stk.pop())) : 
                    return False

        return not stk
