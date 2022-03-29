#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int minimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        
    }
};

int main() {
    Solution sol = Solution();
    cout << (2 == sol.minimumWhiteTiles("10110101", 2, 2) ? "True" : "False") << endl;
    cout << (0 == sol.minimumWhiteTiles("11111", 2, 3) ? "True" : "False") << endl;
    return 0;
}