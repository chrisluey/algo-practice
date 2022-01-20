class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder result = new StringBuilder();
        int i = 1, j = 1, carry = 0;
        while (i <= num1.length() || j <= num2.length()) {
            if (i > num1.length()) {
                char curr2 = num2.charAt(num2.length() - j);
                int int2 = curr2 - 48;
                if (carry == 1 && int2 == 9) {
                    int2 = 0;
                    carry = 1;
                } else {
                    int2 += carry;
                    carry = 0;
                }
                result.append((char)( int2 + '0'));
                j++;
                continue;
            } else if (j > num2.length()) {
                char curr1 = num1.charAt(num1.length() - i);
                int int1 = curr1 - 48;
                if (carry == 1 && int1 == 9) {
                    int1 = 0;
                    carry = 1;
                } else {
                    int1 += carry;
                    carry = 0;
                }
                result.append((char)( int1 + '0'));
                i++;
                continue;
            }
            char curr1 = num1.charAt(num1.length() - i);
            char curr2 = num2.charAt(num2.length() - j);
            int int1 = curr1 - 48;
            int int2 = curr2 - 48;
            int combo = int1 + int2 + carry;
            if (combo >= 10) {
                carry = 1;
                combo -= 10;
            } else {
                carry = 0;
            }
            
            result.append((char)( combo + '0'));
            i++;
            j++;
        }
        if (carry == 1) {
            result.append('1');
        }
        return result.reverse().toString();
    }
}