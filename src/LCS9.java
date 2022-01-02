class Solution {
    public boolean isPalindrome(int x) {
        int n = 0;
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        while (n < x) {
            n = n * 10 + x % 10;
            x = x / 10;
        }
        return x == n || x == n / 10;
    }
}