class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_substring = 0
        l = 0
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            
            substring.add(s[r])
            max_substring = max(max_substring,len(substring))
            
        return max_substring