class Solution {
    public int lengthOfLastWord(String s) {
        // int lastSpace = s.lastIndexOf(" ");
        // return s.length() - 1 - lastSpace;
        String[] arr = s.split(" ");
        if (arr.length > 0) {
            return arr[arr.length - 1].length();
        } else {
            return 0;        
        }
    }
}