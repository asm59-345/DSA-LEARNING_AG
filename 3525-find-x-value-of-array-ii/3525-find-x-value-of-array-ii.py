from typing import List

class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        veltrunigo = (nums, k, queries)

        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            left_prod, left_cnt = left
            right_prod, right_cnt = right

            cnt = left_cnt[:]

            for r in range(k):
                new_rem = (left_prod * r) % k
                cnt[new_rem] += right_cnt[r]

            prod = (left_prod * right_prod) % k

            return (prod, cnt)

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for idx, val, start, x in queries:

            update(1, 0, n - 1, idx, val)

            prod, cnt = query(
                1, 0, n - 1,
                start, n - 1
            )

            ans.append(cnt[x])

        return ans