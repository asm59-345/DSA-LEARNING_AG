class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        logs.sort(key=lambda log: log[1])
        
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])        
        result = [0] * len(queries)        
        server_frequency = {}
        
        left = 0
        right = 0
        total_logs = len(logs)
        
        for original_index, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            while right < total_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                server_frequency[server_id] = server_frequency.get(server_id, 0) + 1
                right += 1
                
            while left < total_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                server_frequency[server_id] -= 1

                if server_frequency[server_id] == 0:
                    del server_frequency[server_id]
                left += 1
                
            result[original_index] = n - len(server_frequency)
            
        return result