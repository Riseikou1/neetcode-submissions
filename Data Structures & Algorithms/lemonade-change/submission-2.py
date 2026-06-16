class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur_fives = 0
        cur_tens = 0

        for bill in bills :
            bill -= 5
            if not bill :
                cur_fives += 1
            elif bill == 5 :
                cur_tens += 1
                while cur_fives and bill >= 5 :
                    cur_fives -= 1
                    bill -= 5
                if bill : return False
            else :
                if cur_tens :
                    bill -= 10
                    cur_tens -= 1
                while cur_fives and bill >= 5 :
                    cur_fives -= 1
                    bill -= 5
                if bill : return False

        return True
