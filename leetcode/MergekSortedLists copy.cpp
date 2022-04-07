/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // init a priority queue to store pointers to the current nodes of each list together
        // init pqueue with the front nodes of each list
        // init a node to hold the result
        // while loop until pqueue not empty
        //      get the min pointer of the pqueue
        //      put the pointer to the result linked list
        //      if the next of this pointer is not null, put it into pqueue
        // return the result
        auto cmp = [](ListNode* left, ListNode* right) {
            return left->val > right->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pqueue(cmp);
        ListNode* res = nullptr;
        ListNode** tail = nullptr;
        for (auto l : lists) {
            if (l != nullptr) {
                pqueue.push(l);
            }
        }
        while (!pqueue.empty()) {
            auto l = pqueue.top();
            pqueue.pop();
            if (res == nullptr) {
                res = new ListNode(l->val, nullptr);
                tail = &res->next;
            } else {
                *tail = new ListNode(l->val, nullptr);;
                tail = &(*tail)->next;
            }

            l = l->next;
            if (l != nullptr) {
                pqueue.push(l);
            }
        }
        return res;
    }
};

int main() {
    return 0;
}