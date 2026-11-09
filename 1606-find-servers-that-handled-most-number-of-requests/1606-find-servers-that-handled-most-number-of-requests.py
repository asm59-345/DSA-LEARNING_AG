class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq
        tree = [0] * (k+1)

        def update (i, val):
            i+= 1
            while i<= k:
                tree[i] += val
                i  += i & -i

        def query(i):
            s = 0
            while i> 0:
                s += tree[i]
                i -= i & -i
            return s

        def find(rank):
            idx = 0
            bit = 1 << (k.bit_length()  -1)

            while bit:
                nxt = idx + bit
                if nxt <= k and tree[nxt] < rank:
                    idx = nxt
                    rank -= tree[nxt]
                bit >>= 1
            return idx 

        for i in range(k):
            update(i,1)
        busy = []
        count = [0] * k

        for i , t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, server = heapq.heappop(busy)
                update(server,1)

            total = query(k)
            if total == 0:
                continue
            start = i % k
            before = query(start)

            if total > before:
                server = find(before + 1)
            else:
                server = find(1)

            update(server, -1)
            count[server] += 1

            heapq.heappush(busy, (t + load[i], server ))
        maxium = max (count)
        
        return [i for i, c in enumerate(count) if c == maxium]