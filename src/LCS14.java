class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        }
        String first = strs[0];
        String result = "";
        for (int k = 1; k <= first.length(); k++) {
            String curr = first.substring(0,k);
            int loop = 1;
            for (int i = 1; i < strs.length; i++) {
                if (!strs[i].startsWith(curr)) {
                    loop = 0;
                    break;
                }
            }
            if (loop == 1 && curr.length() > result.length()) {
                result = curr;
            }
        }
            
        return result;
    }
}