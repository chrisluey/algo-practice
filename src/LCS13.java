class Solution {
    public int romanToInt(String s) {
        int i = 0;
        int result = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            System.out.println(c);
            switch(c) {
                case 'I':
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'V') {
                            result += 4;
                            i += 2;
                        } else if (s.charAt(i + 1) == 'X') {
                            result += 9;
                            i += 2;
                        } else {
                            result += 1;
                            i++;
                        }
                    } else {
                        result += 1;
                        i++;
                    }
                    break;
                case 'V':
                    result += 5;
                    i++;
                    break;
                case 'X':
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'L') {
                            result += 40;
                            i += 2;
                        } else if (s.charAt(i + 1) == 'C') {
                            result += 90;
                            i += 2;
                        } else {
                            result += 10;
                            i++;
                        }
                    } else {
                        result += 10;
                        i++;
                    }
                    break;
                case 'L':
                    result += 50;
                    i++;
                    break;
                case 'C':
                    if (i + 1 < s.length()) {
                        if (s.charAt(i + 1) == 'D') {
                            result += 400;
                            i += 2;
                        } else if (s.charAt(i + 1) == 'M') {
                            result += 900;
                            i += 2;
                        } else {
                             result += 100;
                            i++;
                        }
                    } else {
                        result += 100;
                        i++;
                    }
                    break;
                case 'D':
                    result += 500;
                    i++;
                    break;
                case 'M':
                    result += 1000;
                    i++;
                    break;
                default:
                    i++;
                    break;
            }
        }
        return result;
    }
}