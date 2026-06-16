class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temuujin = {}

        for word in strs :
            key = ''.join(sorted(word))
            if key not in temuujin :
                temuujin[key] = []
            temuujin[key].append(word)
        
        return list(temuujin.values())