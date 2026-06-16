class TimeMap:

    def __init__(self):
        self.temuujin = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.temuujin[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.temuujin : return ""

        value = self.temuujin[key]
        res = ""
        l,r = 0,len(value)-1
        while l <= r:
            m = (r+l)//2
            if value[m][0] <= timestamp :
                res = value[m][1]
                l = m + 1
            else :
                r = m - 1

        return res


        
