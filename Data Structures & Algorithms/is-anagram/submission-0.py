class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = dict()
        seen_t = dict()
        if len(s) != len(t):
            return False 
        else:
            for letter in s:
                if letter not in seen_s:
                    seen_s[letter] = 1
                else:
                    seen_s[letter] += 1
            for letter in t:
                if letter not in seen_t:
                    seen_t[letter] = 1
                else:
                    seen_t[letter] += 1
            if seen_s == seen_t:
                return True 
            else:
                return False



                
            

