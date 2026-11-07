import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for available servers: stores (weight, index)
        available = []
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))
            
        # Min-heap for unavailable servers: stores (free_time, weight, index)
        unavailable = []
        
        ans = []
        current_time = 0
        
        for j, duration in enumerate(tasks):
            # Tasks arrive at second j
            current_time = max(current_time, j)
            
            # Release all servers that finish by the current time
            while unavailable and unavailable[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, idx))
                
            # If no servers are available, jump time directly to the next freeing server
            if not available:
                current_time = unavailable[0][0]
                while unavailable and unavailable[0][0] <= current_time:
                    free_time, weight, idx = heapq.heappop(unavailable)
                    heapq.heappush(available, (weight, idx))
                    
            # Assign the task to the best available server
            weight, idx = heapq.heappop(available)
            ans.append(idx)
            
            # Mark the server as busy until current_time + duration
            heapq.heappush(unavailable, (current_time + duration, weight, idx))
            
        return ans