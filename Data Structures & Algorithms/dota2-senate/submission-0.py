class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire, radiant = deque(), deque()
        n = len(senate)
        for idx, char in enumerate(senate) :
            if char == 'R' :
                radiant.append(idx)
            else :
                dire.append(idx)

        while dire and radiant :
            dire_turn = dire.popleft()
            radiant_turn = radiant.popleft()
            if dire_turn < radiant_turn :
                dire.append(dire_turn + n)
            else :
                radiant.append(radiant_turn + n)

        return "Radiant" if radiant else "Dire"
