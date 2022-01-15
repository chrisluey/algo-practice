class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() == 0) {
            return true;
        }
        if (t.length() == 0) {
            return false;
        }
        int i = 0, j = 0, k = 0;
        for (; i < s.length(); i++) {
            while (j < t.length()) {
                if (s[i] == t[j]) {
                    j++;
                    if (i == s.length() - 1) {
                        k++;
                    }
                    break;
                } else {
                    j++;
                }
            }
            if (j == t.length()) {
                break;
            }
        }
        return k > 0;
    }
};