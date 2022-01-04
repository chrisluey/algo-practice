class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while (true) {
            int curr = 0;
            while (n > 0) {
                curr += Math.pow(n % 10, 2);
                n = n / 10;
            }
            if (curr == 1) {
                return true;
            } else if (set.contains(curr)) {
                return false;
            } else {
                set.add(curr);
            }
            n = curr;
        }
    }
}