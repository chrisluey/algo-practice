class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        }
        double doub = log10(n) / log10(3);
        return std::trunc(doub) == doub;
    }
};