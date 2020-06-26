/**
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
         map<ListNode*,int> freq;
        while(head!=nullptr){
            if(freq.find(head)==freq.end()){
                freq.insert(make_pair(head,1));
                head=head->next;
            }
            else{
                return true;
            }
            
        }
        return false;
    }
};
