// https://leetcode.com/problems/maximum-subarray/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curSum=0, maxSum= nums[0], i, n=nums.size();
        for(i=0; i<n; i++){
            curSum=max(nums[i], curSum+nums[i]);
            maxSum= max(curSum, maxSum);
        }
        return maxSum;
    }
};
