class Solution {
public:
    char findTheDifference(string s, string t) {
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            result += int(s[i]);
        }
        for (int i = 0; i < t.length(); i++) {
            result -= int(t[i]);
        }
        return (char)abs(result);
    }
};