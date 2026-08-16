class Solution:

    def encode(self, strs: List[str]) -> str:

        coded = ""

        for s in strs:
            length = len(s)
            coded += f"{length}#{s}"
        return coded

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
        # word starts at j+1, goes for `length` characters
        # ... slice it, append to result, then move i past it

            result.append(s[j+1:j+1+length])
            i = j + 1 + length

        return result
        




             