# ver 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             try:
#                 if i != nums.index(target - nums[i]):
#                     return [i, nums.index(target - nums[i])]
#             except ValueError:
#                 continue


# ver 2，比 ver 1 更优秀
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                index = nums.index(target - nums[i])
            except ValueError:
                continue
            if i != index:
                return [i, index]