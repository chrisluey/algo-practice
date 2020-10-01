class Solution {
    public String intToRoman(int num) {
        String s = "";
        return intToRomanRecursive(num, s);
    }
    
    public String intToRomanRecursive(int num, String s) {
        if (num == 0) {
            return s;
        } else if (num >= 1000) {
            s += "M";
            return intToRomanRecursive(num - 1000, s);
        } else if (num >= 900) {
            s += "CM";
            return intToRomanRecursive(num - 900, s);
        } else if (num >= 500) {
            s += "D";
            return intToRomanRecursive(num - 500, s);
        } else if (num >= 400) {
            s += "CD";
            return intToRomanRecursive(num - 400, s);
        } else if (num >= 100) {
            s += "C";
            return intToRomanRecursive(num - 100, s);
        } else if (num >= 90) {
            s += "XC";
            return intToRomanRecursive(num - 90, s);
        } else if (num >= 50) {
            s += "L";
            return intToRomanRecursive(num - 50, s);
        } else if (num >= 40) {
            s += "XL";
            return intToRomanRecursive(num - 40, s);
        } else if (num >= 10) {
            s += "X";
            return intToRomanRecursive(num - 10, s);
        } else if (num >= 9) {
            s += "IX";
            return intToRomanRecursive(num - 9, s);
        } else if (num >= 5) {
            s += "V";
            return intToRomanRecursive(num - 5, s);
        } else if (num >= 4) {
            s += "IV";
            return intToRomanRecursive(num - 4, s);
        } else if (num >= 1) {
            s += "I";
            return intToRomanRecursive(num - 1, s);
        }
        return s;
    }
}