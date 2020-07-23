/*
https://leetcode.com/problems/house-robber/
Runtime: 0 ms, faster than 100.00% of C++ online submissions for House Robber.
Memory Usage: 7.7 MB, less than 80.36% of C++ online submissions for House Robber.
*/


class Solution {
public:
    int rob(vector<int>& nums) {
        int n= nums.size();
        if(n==0)
            return 0;
        if(n==1)
            return nums[0];
        int dp[n], i;
        dp[0]=nums[0];
        dp[1]=max(nums[0], nums[1]);
        for(i=2; i<n; i++)
            dp[i]= max(nums[i]+dp[i-2], dp[i-1]);
        return dp[n-1];
    }
};
