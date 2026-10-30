class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
    
        if k < 1:
            return -1
        
        # Base case: single node graph
        if n == 1:
            return 0

        # Build adjacency list: u -> list of (v, weight)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # dist[u][cnt] holds the minimum distance to reach node u
        # with cnt consecutive identical characters ending at u.
        # cnt ranges from 1 to k.
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Priority queue stores tuples of: (cost, u, consecutive_count)
        pq = [(0, 0, 1)]
        dist[0][1] = 0

        while pq:
            d, u, count = heapq.heappop(pq)

            # If we reached the target node, this is the minimal valid cost
            if u == n - 1:
                return d

            # If we found a strictly better distance for this state already, skip
            if d > dist[u][count]:
                continue

            curr_char = labels[u]

            for v, weight in adj[u]:
                next_char = labels[v]

                if next_char == curr_char:
                    next_count = count + 1
                else:
                    next_count = 1

                # Check consecutive limit constraint
                if next_count <= k:
                    new_dist = d + weight
                    if new_dist < dist[v][next_count]:
                        dist[v][next_count] = new_dist
                        heapq.heappush(pq, (new_dist, v, next_count))

        return -1