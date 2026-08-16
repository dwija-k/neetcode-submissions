class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        top = ""
        pairs = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False 
        if not stack:
            return True
        else:
            return False
                



            

        