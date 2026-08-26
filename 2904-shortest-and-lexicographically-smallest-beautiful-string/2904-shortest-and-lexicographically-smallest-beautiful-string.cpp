class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.length();
        string ans = "";
        int min_len = n+1;

        int count = 0;
        int left = 0;

        for (int right = 0; right <n ; ++right){

            if (s[right] == '1'){
                count++;
            }
            while(count == k ){
                while(s[left] == '0'){
                     left++;

                }
            int curr_len = right - left +1;
            string curr_sub = s.substr(left, curr_len);

            if(curr_len < min_len){
                min_len = curr_len;
                ans = curr_sub;

            } else if (curr_len == min_len){
                ans = min(ans, curr_sub);

            }
            if(s[left] == '1'){
                count--;
            }
            left++;

            }
            
        }
        return ans;

    }

};