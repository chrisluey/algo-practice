class Solution {
    public String addBinary(String a, String b) {
        String result = "";
        int carry = 0;
        int length = Math.min(a.length(),b.length());
        for(int i = 1; i <= length; i++) {
            char a_char = a.charAt(a.length()- i);
            char b_char = b.charAt(b.length() - i);
            if (a_char == b_char && a_char == '1') {
                if (carry == 1) {
                    result = "1" + result;
                } else {
                    result = "0" + result;
                }
                carry = 1;
            } else if (a_char == b_char && a_char == '0') {
                if (carry == 1) {
                    result = "1" + result;
                    carry = 0;
                } else {
                    result = "0" + result;
                }
            } else {
                if (carry == 1) {
                    result = "0" + result;
                } else {
                    result = "1" + result;
                }
            }
        }
        
        if (a.length() > b.length()) {
            for (int i = b.length() + 1; i <= a.length(); i++) {
                char a_char = a.charAt(a.length() - i);
                if (carry == 1) {
                    if (a_char == '1') {
                        result = "0" + result;
                    } else {
                        result = "1" + result;
                        carry = 0;
                    }
                } else {
                    result = String.valueOf(a_char) + result;
                }
            }
        } else if (b.length() > a.length()) {
            for (int i = a.length() + 1; i <= b.length(); i++) {
                char b_char = b.charAt(b.length() - i);
                if (carry == 1) {
                    if (b_char == '1') {
                        result = "0" + result;
                    } else {
                        result = "1" + result;
                        carry = 0;
                    }
                } else {
                    result = String.valueOf(b_char) + result;
                }
            }
        }
        if (carry == 1) {
            result = "1" + result;
        }
        return result;
        
    }
}