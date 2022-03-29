#include <vector>
#include <iostream>
#include <map>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        map<string, int> d;
        for (auto w : words) {
            auto it = d.find(w);
            if (it != d.end()) {
                it->second++;
            }
            else {
                d[w] = 1;
            }
        }
        int k = words[0].length();
        int n = words.size();
        vector<int> res;
        if (s.length() < n * k) return res;

        map<string, int> tmpD;

        for (int i = 0; i < s.length() - n * k + 1; ++i) {
            for (auto it : d) {
                tmpD[it.first] = it.second;
            }
            bool isMatch = true;
            for (int j = 0; j < n; ++j) {
                auto w = s.substr(i + j*k, k);
                if ((tmpD.find(w) == tmpD.end()) || (tmpD[w] == 0)) {
                    isMatch = false;
                    break;
                } else {
                    --tmpD[w];
                }
            }
            if (isMatch) {
                res.push_back(i);
            }
        }
        return res;
    }
};

int main() {
    return 0;
}