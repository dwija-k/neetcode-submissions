class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        seen = {}
        for num in nums:
            count = 0
            pairs = [0,0]
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1 
            count += 1
        sorted_pairs = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        return[pair[0] for pair in sorted_pairs[:k]]

            
            