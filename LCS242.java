import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        
        HashMap<Character, Integer> mapS = new HashMap();
        HashMap<Character, Integer> mapT = new HashMap();
        
        for(int i = 0; i < s.length(); i++)
        {
            char cs = s.charAt(i);
            char ct = t.charAt(i);
            
            if (mapS.containsKey(cs))
                mapS.replace(cs, mapS.get(cs) + 1);
            else
                mapS.put(cs,1);
            
            if (mapT.containsKey(ct))
                mapT.replace(ct, mapT.get(ct) + 1);
            else
                mapT.put(ct, 1);
        }
        
        return mapS.equals(mapT);
    }
}