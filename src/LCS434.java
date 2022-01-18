class Solution {
    public int countSegments(String s) {
        if (s.length() == 0)
            return 0;
        // return s.split("\\s+").length;
        int result = 0, space = 0;
        for (char c: s.toCharArray()) {
            if (c == ' ') {
                space = 0;
            } else if (space == 0) {
                result++;
                space = 1;
            }
        }
        return result;
    }
}