import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to track busy servers: stores tuples of (release_time, server_id)
        busy = []
        
        # SortedList to keep track of currently available server IDs efficiently
        available = SortedList(range(k))
        
        # Track how many requests each server handled
        request_count = [0] * k
        
        for i, arr_time in enumerate(arrival):
            # 1. Free up servers whose tasks have finished by the current arrival time
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            # If no servers are available, drop this request
            if not available:
                continue
                
            # 2. Find the first available server >= (i % k)
            preferred = i % k
            idx = available.bisect_left(preferred)
            
            # If no server >= preferred is available, wrap around to the beginning (index 0)
            if idx == len(available):
                idx = 0
                
            server_id = available[idx]
            
            # 3. Assign the request to this server
            available.remove(server_id)
            heapq.heappush(busy, (arr_time + load[i], server_id))
            request_count[server_id] += 1
            
        # 4. Find the server(s) with the maximum request count
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]