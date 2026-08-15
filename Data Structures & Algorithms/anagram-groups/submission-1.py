class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        i = 0
        key_values = {}

        for i in range(len(strs)):
            
            s = strs[i]
            seen = dict()

            for letter in s:
                if letter not in seen:
                    seen[letter] = 1
                else:
                    seen[letter] += 1

            key = tuple(sorted(seen.items()))

            if key not in key_values:
                key_values[key] = []

            key_values[key].append(s)

        return(list(key_values.values()))




        