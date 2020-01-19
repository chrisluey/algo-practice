class Solution {
public:
    string reverseString(string s) {
        string result = "";
        std::string::reverse_iterator rt;
        for (rt = s.rbegin(); rt != s.rend(); rt++)
            result += *rt;
        return result;
    }
};