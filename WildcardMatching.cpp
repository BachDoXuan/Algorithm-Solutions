#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length();
        int m = p.length();

        if (n == 0) {
            for (auto ch : p) {
                if (ch != '*') {
                    return false;
                }
            }
            return true;
        } else if (m == 0) {
            return false;
        }
        bool dpTable[m+1][n+1];
        memset(dpTable, 0, sizeof dpTable);
        dpTable[m][n] = true;

        int dpMaxColMatchIndice[m+1];
        for (int i = 0; i <= m; ++i) {
            dpMaxColMatchIndice[i] = n;
        }

        for (int r = m-1; r >= 0; --r) {
            char pCh = p[r];
            if (pCh == '*') {
                for (int i = max(dpMaxColMatchIndice[r+1]+1, 0); i < n; ++i) {
                    dpTable[r][i] = false;
                }
                for (int i = 0; i <= dpMaxColMatchIndice[r+1]; ++i) {
                    dpTable[r][i] = true;
                }
                dpMaxColMatchIndice[r] = dpMaxColMatchIndice[r+1];
            } else if (pCh == '?') {
                for (int i = n-1; i >= 0; --i) {
                    dpTable[r][i] = dpTable[r+1][i+1];
                }
                dpMaxColMatchIndice[r] = dpMaxColMatchIndice[r+1] - 1;
            } else {
                dpMaxColMatchIndice[r] = -1;
                for (int i = n-1; i >= 0; --i) {
                    if (pCh == s[i] && dpTable[r+1][i+1]) {
                        dpTable[r][i] = true;
                        if (dpMaxColMatchIndice[r] == -1) {
                            dpMaxColMatchIndice[r] = i;
                        }
                    }
                }
            }
        }
        return dpTable[0][0];
    }
};

int main() {
    Solution sol = Solution();
    cout << (sol.isMatch("aa", "a") ? "true" : "false") << endl;
    cout << (sol.isMatch("aa", "*") ? "true" : "false") << endl;
    cout << (sol.isMatch("cb", "?a") ? "true" : "false") << endl;
    cout << (sol.isMatch("aa", "aa") ? "true" : "false") << endl;
    cout << (sol.isMatch("baabba", "?*?a??") ? "true" : "false") << endl;
    return 0;
}