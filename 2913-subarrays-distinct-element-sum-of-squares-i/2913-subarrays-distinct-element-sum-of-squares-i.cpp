class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;

        for (int i = 0; i < n; i++) {
            unordered_set<int> distinctSet;

            for (int j = i; j < n; j++) {
                distinctSet.insert(nums[j]);
                int count = distinctSet.size();
                totalSum += count * count;
            }
        }

        return totalSum;
    }
};