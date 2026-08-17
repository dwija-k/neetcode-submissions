class Solution:
    def isPalindrome(self, s: str) -> bool:

        left_pointer = 0
        right_pointer = len(s)-1

        s = s.lower()

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
            elif not s[right_pointer].isalnum():
                right_pointer -= 1
            elif s[left_pointer] != s[right_pointer]:
                return False
            else:
                left_pointer += 1 
                right_pointer -= 1
        return True
        