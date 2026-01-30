class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def backtrack(start , path):
            subset.append(path[:])

            for i in range(start , len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()            

        backtrack(0, [])
        return subset

        
