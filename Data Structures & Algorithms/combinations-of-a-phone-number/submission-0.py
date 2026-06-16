class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits : return res
        temuujin = {}

        temuujin[2] = ['a', 'b','c']
        temuujin[3] = ['d', 'e','f']
        temuujin[4] = ['g', 'h','i']
        temuujin[5] = ['j', 'k','l']
        temuujin[6] = ['m', 'n','o']
        temuujin[7] = ['p', 'q','r','s']
        temuujin[8] = ['t', 'u','v']
        temuujin[9] = ['w', 'x','y','z']

        def dfs(idx, cur_path) :
            if len(cur_path) == len(digits) :
                res.append("".join(cur_path))
                return 

            for i in range(idx, len(digits)) :
                paths = temuujin[int(digits[idx])]
            
                for j in range(len(paths)) :
                    cur_path.append(paths[j])
                    dfs(i + 1, cur_path)
                    cur_path.pop()

        dfs(0, [])
        return res