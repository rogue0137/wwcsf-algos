/*
https://leetcode.com/problems/valid-parentheses/
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Valid Parentheses.
Memory Usage: 6.4 MB, less than 36.20% of C++ online submissions for Valid Parentheses.
*/
class Solution {
public:
    bool isValid(string s) {
        if(s.size()==0)       //return true if string is empty
            return true;
        if(s.size()%2==1)     //return false if string has odd number of elements
            return false;
        stack<char> st;
        int i=0;
        if(s[i]==')' || s[i]==']' || s[i]=='}')   //return false if string begins with a closing paranthesis
            return false;
        while(s[i]!='\0'){
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
                st.push(s[i]);
            else{
                switch(s[i]){
                    case ')': if(st.top()!='(')
                                   return false;
                              st.pop();
                              break;
                    case ']': if(st.top()!='[')
                                   return false; 
                              st.pop();
                              break;
                    case '}': if(st.top()!='{')
                                   return false; 
                              st.pop();
                              break;
                }
            }
            i++;
        }
        if(st.empty())
            return true;
        else
            return false;
    }
};
