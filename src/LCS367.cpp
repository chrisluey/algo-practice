class Solution {
public:
    bool isPerfectSquare(int num) {
        int i = 1;
        while (i <= 46340) {
            int curr = i * i;
            if (curr == num) {
                return true;
            } else if (curr > num) {
                return false;
            }
            i++;
        }
        return false;
    }
};