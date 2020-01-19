import java.util.HashMap;
import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        List<String> bannedList = Arrays.asList(banned);
        
        
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
        
        String[] paragraphArray = paragraph.split("[ !?',;.]+");
        
        for (String word: paragraphArray) {
            String lowercase = word.toLowerCase();
            if (!bannedList.contains(lowercase)) {
                if (hashMap.get(lowercase) == null) {
                    hashMap.put(lowercase, 1);
                } else {
                    hashMap.put(lowercase, hashMap.get(lowercase) + 1);
                }
            }
        }
        
        Iterator iterator = hashMap.entrySet().iterator();
        
        Map.Entry<String, Integer> result = null;
        while (iterator.hasNext()) {
            Map.Entry<String, Integer> next = (Map.Entry)iterator.next();
            if (result == null) {
                result = next;
            } else if (next.getValue() >= result.getValue()) {
                result = next;
            }
        }
        
        return result.getKey();
        
    }
}