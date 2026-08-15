class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int n = words.size();
        int i = 0;

        while (i < n) {
            int j = i;
            int lineLen = 0;

            while (j < n && lineLen + words[j].size() + (j - i) <= maxWidth) {
                lineLen += words[j].size();
                j++;
            }
            int numWords = j - i;
            int numSpaces = maxWidth - lineLen;
            string line = "";
         
            if (j == n || numWords == 1) {
                for (int k = i; k < j; k++) {
                    line += words[k];
                    if (k < j - 1) line += " ";
                }
                line.append(maxWidth - line.size(), ' ');
            } else {
               
                int baseSpaces = numSpaces / (numWords - 1);
                int extraSpaces = numSpaces % (numWords - 1);

                for (int k = i; k < j; k++) {
                    line += words[k];
                    if (k < j - 1) {
                        int spacesToAdd = baseSpaces + (k - i < extraSpaces ? 1 : 0);
                        line.append(spacesToAdd, ' ');
                    }
                }
            }
            res.push_back(line);
            i = j;
        }
        return res;
    }
};