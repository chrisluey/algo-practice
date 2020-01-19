class Solution {
    public String reverseWords(String s) {
        String[] stringArray = s.split(" ");
        
        for(int i = 0; i < stringArray.length; i++)
        {
            StringBuilder sb = new StringBuilder(stringArray[i]);
            stringArray[i] = sb.reverse().toString();
        }
        
        s = String.join(" ", stringArray);
        
        return s;
    }
}