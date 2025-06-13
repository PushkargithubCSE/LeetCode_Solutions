// logic used = expected sum of number - actual sum of numbers
class Solution {
public:
    int missing_number;
    int i;
    int actual_sum;
    int expected_sum;

    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        expected_sum = n * (n + 1) / 2;
        actual_sum = 0;

        for (i = 0; i < n; i++) {
            actual_sum += nums[i];
        }

        missing_number = expected_sum - actual_sum;
        return missing_number;
    }
};
