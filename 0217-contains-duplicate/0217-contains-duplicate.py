class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result=set()
        for num in nums:
            if num in result:
                return True
            result.add(num)
        return False

