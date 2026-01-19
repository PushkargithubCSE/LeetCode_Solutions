class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memory = set()
        i = 0

        for j in range(len(nums)):
            if j - i > k:
                memory.remove(nums[i])
                i += 1

            if nums[j] in memory:
                return True

            memory.add(nums[j])

        return False
