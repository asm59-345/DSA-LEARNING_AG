from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Pair each query with its original index so we can restore the order later
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_count = {} # Maps server_id -> frequency in the current window
        
        left = 0
        right = 0
        l_logs = len(logs)
        
        for q_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            # Expand the right pointer to include logs up to window_end
            while right < l_logs and logs[right][1] <= window_end:
                s_id = logs[right][0]
                server_count[s_id] = server_count.get(s_id, 0) + 1
                right += 1
                
            # Shrink the left pointer to remove logs older than window_start
            while left < l_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_count[s_id] -= 1
                if server_count[s_id] == 0:
                    del server_count[s_id]
                left += 1
                
            # Servers with 0 requests = Total servers - servers that received requests
            ans[q_idx] = n - len(server_count)
            
        return ans