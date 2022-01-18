class Solution {
    
    List<String> result;
    String[] mapping = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        result = new ArrayList();
        addCombos("", digits);
        return result;
    }
    
    public void addCombos(String num, String digits) {
        if (digits.length() == 0)
            return;
        char curr = digits.charAt(0);
        int currNum = Character.getNumericValue(curr);
        String currMapping = mapping[currNum];
        if (digits.length() == 1) {
            for (int i = 0; i < currMapping.length(); i++) {
                result.add(num + currMapping.charAt(i));
            }
            return;
        } else {
            for (int i = 0; i < currMapping.length(); i++) {
                addCombos(num + currMapping.charAt(i), digits.substring(1));
            }
        }
    }
}