from collections import defaultdict
from typing import List


class Solution:

    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        # Sort logs chronologically by timestamp
        logs.sort(key=lambda log: log[1])

        # Store queries with their original indices and sort them by query time
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])

        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        distinct_active = 0

        left = 0
        right = 0
        m = len(logs)

        for orig_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time

            # Add all requests that arrived up to window_end
            while right < m and logs[right][1] <= window_end:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    distinct_active += 1
                server_counts[s_id] += 1
                right += 1

            # Remove all requests that arrived strictly before window_start
            while left < m and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    distinct_active -= 1
                left += 1

            # Number of inactive servers = total - distinct active
            ans[orig_idx] = n - distinct_active

        return ans


