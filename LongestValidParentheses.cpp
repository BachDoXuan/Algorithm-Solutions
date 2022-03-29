#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
    typedef struct {
        char c;
        int idx;
    } Position;
public:
    int longestValidParentheses(string s) {
        stack<Position> stk;
        int longest = 0;
        for (int i=0; i < s.length(); ++i) {
            char c = s[i];
            if (stk.empty()) {
                stk.push({c, i});
            } else {
                Position top = stk.top();
                if (top.c == '(' && c == ')') {
                    stk.pop();
                } else {
                    stk.push({c, i});
                }
            }
        }
        int idx = s.length();
        while (!stk.empty()) {
            Position top = stk.top();
            stk.pop();
            if (idx - top.idx - 1 > longest) {
                longest = idx - top.idx - 1;
            }
            idx = top.idx;
        }
        if (idx > longest) {
            longest = idx;
        }

        return longest;
    }
};

int main() {
    return 0;
}