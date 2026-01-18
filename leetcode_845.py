#Longest Mountain in array 
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(1, n - 1):
            if arr[i-1] < arr[i] > arr[i+1]:  # peak
                left = []
                right = []

                j = i - 1
                while j >= 0 and arr[j] < arr[j + 1]:
                    left.append(arr[j])
                    j -= 1

                j = i + 1
                while j < n and arr[j] < arr[j - 1]:
                    right.append(arr[j])
                    j += 1

                ans = max(ans, len(left) + 1 + len(right))

        return ans
