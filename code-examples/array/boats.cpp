 
// https://leetcode.com/problems/boats-to-save-people/

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int i=0, j=people.size()-1, count=0;
        while(i <= j){
            count++;
            if(people[j] + people[i] <= limit)
                i++;
            j--;
        }
        return count;
    }
};
