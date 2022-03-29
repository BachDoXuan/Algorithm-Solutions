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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) return head;

        ListNode * ptr = head;
        int count = 1;
        ListNode * prevPtr = new ListNode(0, head);
        ListNode * res = prevPtr;
        ListNode * endPtr = head;
        ListNode *tmpPtr, *tmpEndPtr;

        while (endPtr != nullptr) {
            ++count;
            endPtr = endPtr->next;

            if (count == k+1) {
                count = 1;
                tmpEndPtr = endPtr;
                while (ptr->next != endPtr) {
                    tmpPtr = ptr->next;
                    ptr->next = tmpEndPtr;
                    tmpEndPtr = ptr;
                    ptr = tmpPtr;
                }
                tmpPtr = prevPtr->next;
                prevPtr->next = ptr;
                ptr->next = tmpEndPtr;
                prevPtr = tmpPtr;
                ptr = endPtr;
            }
        }
        ptr = res;
        res = res->next;
        delete ptr;
        return res;
    }
};

int main() {
    return 0;
}