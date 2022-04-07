#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int trap(vector<int>& height) {
        int begin = 0;
        int end = height.size() - 1;
        int trap = 0;
        int k;

        while (begin < end) {
            if (height[begin] <= height[end]) {
                k = begin + 1;
                while (k < end) {
                    if (height[k] <= height[begin]) {
                        trap += height[begin] - height[k];
                        ++k;
                    } else {
                        begin = k;
                        break;
                    }
                }
                if (k == end) {
                    break;
                }
            } else {
                k = end - 1;
                while (k > begin) {
                    if (height[k] <= height[end]) {
                        trap += height[end] - height[k];
                        --k;
                    } else {
                        end = k;
                        break;
                    }
                }
                if (k == begin) {
                    break;
                }
            }
        }
        return trap;
    }
};

int main() {
    return 0;
}