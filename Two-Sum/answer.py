class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
            looking_for = target - nums[i]

            if looking_for in seen:
                return[seen[looking_for],i]
            else:
                seen[value] = i 