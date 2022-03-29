#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
    typedef struct AdjInfo {
        int adj;
        int weight;
    } AdjInfo;

    typedef struct DistanceVertex {
        long long dis;
        int vertex; 
    } DistanceVertex;

public:
    struct cmp {
        bool operator() (DistanceVertex &left, DistanceVertex &right) {
                return left.dis > right.dis;
        }
    };

    void dijkstra(int n, vector<AdjInfo> adjLists[], int src, long long minDistance[]) {
        priority_queue<DistanceVertex, vector<DistanceVertex>, cmp> pqueue;
        pqueue.push({0, src});
        bool visited[n];
        for (int i = 0; i < n; ++i) {
            visited[i] = false;
        }
    
        for (int i = 0; i < n; ++i) {
            minDistance[i] = -1;
        }

        while (!pqueue.empty()) {
            auto top = pqueue.top();
            pqueue.pop();
            if (visited[top.vertex]) {
                continue;
            }
            minDistance[top.vertex] = top.dis;
            visited[top.vertex] = true;
            for (auto adjInfo : adjLists[top.vertex]) {
                if (visited[adjInfo.adj]) {
                    continue;
                } else {
                    pqueue.push({top.dis + adjInfo.weight, adjInfo.adj});
                }
            } 
        }
    }

    long long minimumWeight(int n, vector<vector<int> > & edges, int src1, int src2, int dest) {
        vector<AdjInfo> adjLists[n];
        vector<AdjInfo> reverseAdjLists[n];

        for (auto e : edges) {
            adjLists[e[0]].push_back({e[1], e[2]});
            reverseAdjLists[e[1]].push_back({e[0], e[2]});     
        }

        long long src1Shortest[n];
        dijkstra(n, adjLists, src1, src1Shortest);

        long long src2Shortest[n];
        dijkstra(n, adjLists, src2, src2Shortest);
    
        long long destShortest[n];
        dijkstra(n, reverseAdjLists, dest, destShortest);
        
        long long minWeight = -1;
        long long tmp;
        for (int v = 0; v < n; ++v) {
            if (src1Shortest[v] < 0 || src2Shortest[v] < 0 || destShortest[v] < 0) {
                continue;
            } else {
                tmp = src1Shortest[v] + src2Shortest[v] + destShortest[v];
                if (minWeight < 0 || minWeight > tmp) {
                    minWeight = tmp;
                }
            }
        }
        return minWeight;
    }
};

int main() {
    Solution sol = Solution();
    return 0;
}