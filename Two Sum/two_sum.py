class Solution(object):
    def twoSum(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]
        return []

print(Solution().twoSum([2, 7, 11, 15], 18))