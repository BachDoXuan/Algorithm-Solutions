"""
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.

 

Example 1:


Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Output: 9
Explanation:
The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.
Example 2:


Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Output: -1
Explanation:
The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
 

Constraints:

3 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= fromi, toi, src1, src2, dest <= n - 1
fromi != toi
src1, src2, and dest are pairwise distinct.
1 <= weight[i] <= 105
"""
from typing import List
import heapq


class Solution:
    def dijkstra(self, n: int, adjLists: List[List[int]], src: int) -> List[int]:
        """
        - def dijkstra(n: int, adjLists: List[List[int]], src: int) -> List[int]:
        -       declare priority queue for current distances from src, pqueue for (dis, v)
        -       put (0, src) to pqueue
        -       declare visited list to mark visited for each vertex, init as all Falses
        -       declare minDistance list to hold the min distance from src to each vertex, init as all -1 
        -       while pqueue not empty:
        -           (dis, v) <- extract min from pqueue
        -           if visited[v]: continue
        -           update minDistance[v] = dis
        -           mark visited[v] as True
        -           for all adj vertex u of v:
        -               if visited[u]: continue
        -               put (dis + edge(u,v), u) to pqueue
        -       return minDistance
        """
        pqueue = []
        heapq.heappush(pqueue, (0, src))
        visited = [False for i in range(n)]
        minDistance = [-1 for i in range(n)]
        while pqueue:
            dis, v = heapq.heappop(pqueue)
            if visited[v]:
                continue
            minDistance[v] = dis
            visited[v] = True
            for adj, weight in adjLists[v]:
                if visited[adj]:
                    continue
                heapq.heappush(pqueue, (dis + weight, adj))

        return minDistance

    def minimumWeight(self, n: int, edges: List[List[List[int]]], src1: int, src2: int, dest: int) -> int:
        """
        - From edges, build adjacent list for each vertex of graph G -> List[List[(adjVertex, weight)]]
        - find shortest paths from src1 to each vertex -> src1Shortest (call dijsktra(n, adjLists, src1))
        - find shortest pas from src2 to each vertex -> src2Shortest
        - From edges, build adjacent list of each vertex of the reverse graph of G (rG)
        - for the reverse graph rG of G, find shortest paths from dest to each vertex -> destShortest
        - init minWeight = -1
        - for each vertex v of G,
        -   if src1Shortest[v] or src2Shortest[v] or destShortest[v] is -1, continue
        -   else if minWeight is -1 or larger than src1Shortest[v] + src2Shortest[v] + destShortest[v], update minWeight
        - return minWeight
        """
        adjLists = [[] for i in range(n)]
        reverseAdjLists = [[] for i in range(n)]

        for e in edges:
            adjLists[e[0]].append([e[1], e[2]])
            reverseAdjLists[e[1]].append([e[0], e[2]])

        src1Shortest = self.dijkstra(n, adjLists, src1)
        src2Shortest = self.dijkstra(n, adjLists, src2)
        destShortest = self.dijkstra(n, reverseAdjLists, dest)

        minWeight = -1
        for v in range(n):
            if src1Shortest[v] == -1 or src2Shortest[v] == -1 or destShortest[v] == -1:
                continue
            elif minWeight == -1 or minWeight > src1Shortest[v] + src2Shortest[v] + destShortest[v]:
                minWeight = src1Shortest[v] + src2Shortest[v] + destShortest[v]

        return minWeight

sol = Solution()
print(9 == sol.minimumWeight(6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]],
0, 1, 5))
print(-1 == sol.minimumWeight(3, [[0,1,1],[2,1,1]], 0, 1, 2))