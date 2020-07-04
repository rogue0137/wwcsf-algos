/* Minimum time visiting all points
https://leetcode.com/problems/minimum-time-visiting-all-points/
*/

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int ans=0, i, n=points.size();
        for(i=1; i<n; i++)
            ans+=max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1])); //diagonal steps + horizontal/vertical steps
        return ans;
    }
};
