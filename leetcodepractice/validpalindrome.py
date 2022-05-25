class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Make the entire string lowercase
        #O(n) n is the length of the string
#         lowerCaseString = s.lower()
#         #O(1)
#         sanitizedCharacters = []
#         #O(n) n is the length of the string
#         for c in lowerCaseString:
#             if c.isalnum():
#                 sanitizedCharacters.append(c)
#         #O(n)
#         sanitizedString = ''.join(sanitizedCharacters)
        
#         #compare string with reversed string
#         #O(n)
#         reversedString = ''.join(reversed(sanitizedString))
#         #O(n)
#         if sanitizedString == reversedString:
#             return True
        
#         return False

        l,r = 0, len(s) -1 
    
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l+=1
                    r-=1
        return True