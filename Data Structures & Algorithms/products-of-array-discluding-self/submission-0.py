class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i = 1
        prefix = 1
        suffix = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output



            





        