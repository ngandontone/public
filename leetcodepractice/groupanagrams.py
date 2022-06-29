class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}
        
        for i in range(len(strs)):
            sorted_key = ''.join(sorted(strs[i]))
            if sorted_key in anagram_group:
                anagram_group[sorted_key].append(strs[i])
            else:
                anagram_group[sorted_key] = [strs[i]]
        anagram_groups = []
        for key in anagram_group:
            anagram_groups.append(anagram_group[key])
        
        
        if anagram_groups == None:
            return [['']]
        return anagram_groups 