#include <string>
#include <iostream>

using namespace std;

// class Solution {
// public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        char tmp[numRows][s.length()];
        memset(tmp, 0, sizeof tmp);
        int curR = 0, curC = 0, curIndex = 0;
        bool isDown = true;

        while (curIndex < s.length()) {
            tmp[curR][curC] = s[curIndex];
            ++curIndex;
            if (isDown) {
                if (curR < numRows-1) {
                    ++curR;
                } else {
                    ++curC;
                    --curR;
                    isDown = false;
                }
            } else {
                if (curR > 0) {
                    --curR;
                    ++curC;
                } else {
                    ++curR;
                    isDown = true;
                }
            }
        }

        string res = "";
        for (int r = 0; r < numRows; ++r) {
            for (int c = 0; c < s.length(); ++c) {
                if (tmp[r][c] != '\0') {
                    res += tmp[r][c];
                }
            }
        }
        return res;
    }
// };

int main() {
    cout << convert("PAYPALISHIRING", 3) << endl;
    cout << convert("PAYPALISHIRING", 4) << endl;
    cout << convert("A", 1) << endl;
    return 0;
}