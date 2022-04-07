#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int tmp, tmp2, k;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] <= 0 || nums[i] > nums.size()) {
                nums[i] = 0;
                continue;
            } else if (nums[i] == i+1) {
                continue;
            } else {
                tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                k = nums[i] - 1;
                while (true) {
                    if (tmp > nums.size() || tmp <= 0 || tmp == k+1) {
                        break;
                    }
                    tmp2 = nums[tmp-1];
                    nums[tmp-1] = tmp;
                    k = tmp-1;
                    tmp = tmp2;
                }
            }
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != i+1) {
                return i+1;
            }
        }
        return nums.size() + 1;
    }
};

int main() {
    return 0;
}