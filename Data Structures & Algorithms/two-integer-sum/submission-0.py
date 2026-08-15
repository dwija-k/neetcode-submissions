class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        seen = {}
        output = [0,0]
        i = 0
        j = 0
    
        for i in range(length): 

            value = nums[i]
            difference = target - value 

            if difference in seen: 
                return[seen[difference],i]
            
            seen[value] = i


            
        


        