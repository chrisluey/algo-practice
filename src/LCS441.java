class Solution {
    public int arrangeCoins(int n) {
        int i = 0;
        while (n > 0) {
            i++;
            n -= i;
        }
        if (n < 0) {
            i -= 1;
        }
        return i;
        
    }
}