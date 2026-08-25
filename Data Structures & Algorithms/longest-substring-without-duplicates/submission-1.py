class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        seen = set()
        chars_no = 0
        largest = 0

        while r < len(s):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                chars_no -= 1

            seen.add(s[r])
            chars_no += 1

            if chars_no > largest:
                largest = chars_no
                
            r += 1

        return largest
