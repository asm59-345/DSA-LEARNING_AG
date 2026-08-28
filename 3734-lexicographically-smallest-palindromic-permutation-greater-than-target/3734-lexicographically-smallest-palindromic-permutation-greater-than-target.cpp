class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }

        // 1. Check palindrome feasibility & build half-frequency map
        int odd_count = 0;
        char odd_char = 0;
        vector<int> half_freq(26, 0);

        for (int i = 0; i < 26; ++i) {
            if (freq[i] % 2 != 0) {
                odd_count++;
                odd_char = 'a' + i;
            }
            half_freq[i] = freq[i] / 2;
        }

        if ((n % 2 == 0 && odd_count != 0) || (n % 2 == 1 && odd_count != 1)) {
            return "";
        }

        int m = n / 2;

        // Helper lambda to construct full palindrome from half string
        auto make_pal = [&](const string& half) -> string {
            string res = half;
            if (n % 2 == 1) res += odd_char;
            for (int i = m - 1; i >= 0; --i) {
                res += half[i];
            }
            return res;
        };

        string ans = "";

        // 2. Case A: Try matching target[0...m-1] exactly
        vector<int> prefix_freq(26, 0);
        bool can_exact = true;
        for (int i = 0; i < m; ++i) {
            prefix_freq[target[i] - 'a']++;
        }
        for (int c = 0; c < 26; ++c) {
            if (half_freq[c] < prefix_freq[c]) {
                can_exact = false;
                break;
            }
        }

        if (can_exact) {
            string exact_half = target.substr(0, m);
            string cand = make_pal(exact_half);
            if (cand > target) {
                ans = cand;
            }
        }

        // 3. Case B: Backtrack to find the rightmost index i where a larger char can be placed
        for (int i = m - 1; i >= 0; --i) {
            // Recalculate prefix frequency for target[0...i-1]
            vector<int> p_freq(26, 0);
            for (int j = 0; j < i; ++j) {
                p_freq[target[j] - 'a']++;
            }

            bool valid_prefix = true;
            for (int c = 0; c < 26; ++c) {
                if (half_freq[c] < p_freq[c]) {
                    valid_prefix = false;
                    break;
                }
            }
            if (!valid_prefix) continue;

            // Remaining available characters for index i and beyond
            vector<int> rem_freq(26, 0);
            for (int c = 0; c < 26; ++c) {
                rem_freq[c] = half_freq[c] - p_freq[c];
            }

            // Find smallest character strictly greater than target[i]
            for (int c = target[i] - 'a' + 1; c < 26; ++c) {
                if (rem_freq[c] > 0) {
                    rem_freq[c]--;

                    // Build greedy minimal tail for positions i+1 ... m-1
                    string half = target.substr(0, i);
                    half += (char)('a' + c);
                    for (int k = 0; k < 26; ++k) {
                        half.append(rem_freq[k], 'a' + k);
                    }

                    string cand = make_pal(half);
                    if (ans.empty() || cand < ans) {
                        ans = cand;
                    }
                    break; // Found smallest larger char for this position i
                }
            }
        }

        return ans;
    }
};