class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.map.get(key, [])
        if len(values) == 0 : return res
        l, r = 0, len(values) - 1

        while l < r :
            m = (l + r + 1) // 2
            if values[m][1] <= timestamp :
                l = m 
            else :
                r = m - 1
        
        return values[l][0] if values[l][1] <= timestamp else ""

