class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window protocol 

        i = 0
        curr_sum = 0
        min_sum = float('inf')

        for j in range(len(nums)):

            curr_sum += nums[j]

            while curr_sum >= target:
                min_sum = min(min_sum, j-i+1)
                curr_sum -= nums[i]
                i = i+1

        return 0 if min_sum == float('inf') else min_sum
        


