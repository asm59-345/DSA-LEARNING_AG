class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            if a == b:
                return True

            # KMP prefix function for target b
            pi = [0] * k
            j = 0
            for i in range(1, k):
                while j and b[i] != b[j]:
                    j = pi[j - 1]
                if b[i] == b[j]:
                    j += 1
                pi[i] = j

            # Search b in a + a, without constructing it
            j = 0
            for i in range(2 * k - 1):
                c = a[i % k]
                while j and c != b[j]:
                    j = pi[j - 1]
                if c == b[j]:
                    j += 1
                if j == k:
                    return True
            return False

        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        for k in divisors:
            valid = True
            for start in range(0, n, k):
                if not is_rotation(
                    nums[start:start + k],
                    sorted_nums[start:start + k]
                ):
                    valid = False
                    break

            if valid:
                ans += k

        return ans