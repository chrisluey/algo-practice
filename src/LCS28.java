class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.equals("")) {
            return 0;
        }
        char firstChar = needle.charAt(0);
        int needleLength = needle.length();
        int haystackLength = haystack.length();
        for (int i = 0; i < haystackLength; i++) {
            if (haystack.charAt(i) == firstChar) {
                if (i + needleLength > haystackLength) {
                    continue;
                } else  {
                    // System.out.println(haystack.substring(i, needleLength + i));
                    if (haystack.substring(i, needleLength + i).equals(needle)) {
                        return i;
                    }
                }
            }
        }
        return -1;
    }
}