class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        l, r = 0, len(arr) - 1
        while l < r :
            mid = l + (r - l) // 2
            if arr[mid] >= x :
                r = mid
            else :
                l = mid + 1

        r = l
        l = l - 1
        while len(res) < k :
            if r >= len(arr) : 
                res.append(arr[l])
                l -= 1
                continue
            elif l < 0 : 
                res.append(arr[r])  
                r += 1
                continue
            
            elif abs(arr[l] - x) < abs(arr[r] - x) :
                res.append(arr[l])
                l -= 1

            elif abs(arr[l] - x) > abs(arr[r] - x) :
                res.append(arr[r])
                r += 1
            
            elif abs(arr[l] - x) == abs(arr[r] - x) :
                res.append(arr[l])
                l -= 1
            
        return sorted(res)
