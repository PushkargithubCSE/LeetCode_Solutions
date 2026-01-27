from typing import List
from itertools import accumulate


class NumArray:
    def __init__(self, nums: List[int]):
        # Create a prefix sum array with an initial 0 at the beginning
        # prefix_sums[i] represents the sum of elements from index 0 to i-1
        # This allows us to calculate range sums efficiently
        self.prefix_sums = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements from index left to right (inclusive)
        # Sum[left, right] = prefix_sums[right+1] - prefix_sums[left]
        # This works because:
        # - prefix_sums[right+1] contains sum of elements from 0 to right
        # - prefix_sums[left] contains sum of elements from 0 to left-1
        # - Subtracting gives us the sum from left to right
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
