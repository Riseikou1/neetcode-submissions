class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temuujin = defaultdict(list)

        for s in strs :
            key = ''.join(sorted(s))
            temuujin[key].append(s)

        return list(temuujin.values())