class Solution {
    public int addDigits(int num) {
        
        if (num >= 10) {
            if (num % 9 == 0) {
                return 9;
            } else {
                return num % 9;  
            }
        } else {
            return num;
        }
    }
}