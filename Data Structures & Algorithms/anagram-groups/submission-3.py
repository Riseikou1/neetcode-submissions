class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs :
            chars = [0] * 26
            for char in word :
                chars[ord(char) - ord('a')] += 1
            hash_map[tuple(chars)].append(word)
        
        res = []
        for key, val in hash_map.items() :
            res.append(val)
        
        return res
