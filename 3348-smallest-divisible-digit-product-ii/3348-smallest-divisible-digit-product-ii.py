class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into powers of 2, 3, 5, 7
        temp_t = t
        cnt = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                cnt[p] += 1
                temp_t //= p
        if temp_t > 1:
            return "-1"

        def get_factors(c2, c3, c5, c7):
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)

            d8, c2 = divmod(c2, 3)
            d9, c3 = divmod(c3, 2)

            d4, d2 = divmod(c2, 2)
            d3 = c3
            d6 = 0

            # Combine 2 * 3 -> 6
            if d2 and d3:
                d2, d3, d6 = 0, 0, 1

            # CRITICAL OPTIMIZATION:
            # Replace (4, 3) with (2, 6) to keep digit count same but lower smallest digit
            if d4 and d3:
                d4 -= 1
                d3 -= 1
                d2 += 1
                d6 += 1

            return (
                [2] * d2
                + [3] * d3
                + [4] * d4
                + [5] * c5
                + [6] * d6
                + [7] * c7
                + [8] * d8
                + [9] * d9
            )

        def min_digits_needed(c2, c3, c5, c7):
            return len(get_factors(c2, c3, c5, c7))

        def make_suffix(c2, c3, c5, c7, length):
            factors = get_factors(c2, c3, c5, c7)
            factors.extend([1] * (length - len(factors)))
            factors.sort()
            return "".join(map(str, factors))

        n = len(num)
        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        # Step 2: Track required remaining factors along non-zero prefix of num
        first_zero = num.find("0")
        valid_prefix_len = n if first_zero == -1 else first_zero

        prefix_c = [(cnt[2], cnt[3], cnt[5], cnt[7])]
        for i in range(valid_prefix_len):
            d = int(num[i])
            f = digit_factors[d]
            last = prefix_c[-1]
            prefix_c.append(
                (
                    last[0] - f[0],
                    last[1] - f[1],
                    last[2] - f[2],
                    last[3] - f[3],
                )
            )

        # Return original num if zero-free and digit product already divisible by t
        if first_zero == -1:
            r2, r3, r5, r7 = prefix_c[-1]
            if r2 <= 0 and r3 <= 0 and r5 <= 0 and r7 <= 0:
                return num

        # Step 3: Backtrack from rightmost valid prefix index to try larger candidate digits
        for i in range(valid_prefix_len, -1, -1):
            if i == n:
                continue

            start_d = int(num[i]) + 1 if i < valid_prefix_len else 1

            for d in range(start_d, 10):
                f = digit_factors[d]
                rem2 = prefix_c[i][0] - f[0]
                rem3 = prefix_c[i][1] - f[1]
                rem5 = prefix_c[i][2] - f[2]
                rem7 = prefix_c[i][3] - f[3]

                rem_len = n - 1 - i
                if min_digits_needed(rem2, rem3, rem5, rem7) <= rem_len:
                    suf = make_suffix(rem2, rem3, rem5, rem7, rem_len)
                    return num[:i] + str(d) + suf

        # Step 4: Expand length if no answer of length n exists
        target_len = n + 1
        while True:
            if min_digits_needed(cnt[2], cnt[3], cnt[5], cnt[7]) <= target_len:
                return make_suffix(cnt[2], cnt[3], cnt[5], cnt[7], target_len)
            target_len += 1