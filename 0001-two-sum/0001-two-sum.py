class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             return [i,j]
        
        # reduced the time complexity
       for i in range(len(nums)):
        prod = target - nums[i]
        if prod in nums and nums.index(prod)!=i:
            return [i,nums.index(prod)]