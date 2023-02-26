class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumOfArr = sum(nums)
        leftSum = 0
        for i, v in enumerate(nums):
            if sumOfArr - leftSum - v == leftSum:
                return i
            leftSum += v
        return -1