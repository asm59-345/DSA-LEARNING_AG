#include <vector>
#include <numeric>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    int memo[505][505];
    int pref[505];

    int getSum(int l, int r) {
        return pref[r + 1] - pref[l];
    }

    int dp(int l, int r) {
        if (l == r) return 0;
        if (memo[l][r] != -1) return memo[l][r];

        int res = 0;
        for (int k = l; k < r; ++k) {
            int leftSum = getSum(l, k);
            int rightSum = getSum(k + 1, r);

            if (leftSum < rightSum) {
                res = max(res, leftSum + dp(l, k));
            } else if (leftSum > rightSum) {
                res = max(res, rightSum + dp(k + 1, r));
            } else {
                res = max(res, leftSum + max(dp(l, k), dp(k + 1, r)));
            }
        }

        return memo[l][r] = res;
    }

public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        memset(memo, -1, sizeof(memo));

        pref[0] = 0;
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + stoneValue[i];
        }

        return dp(0, n - 1);
    }
};