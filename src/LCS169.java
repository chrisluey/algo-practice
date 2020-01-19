import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap();
        double length = nums.length;
        int maj = (int)Math.floor(length / 2) + 1;
        for (int i = 0; i < nums.length; i++)
        {
            int x = nums[i];
            if (!map.containsKey(x))
            {
                map.put(x,1);
            }
            else
            {
                map.replace(x, map.get(x) + 1);
            }
            if (map.get(x) >= maj)
            {
                return x;
            }
        }
        return 0;
    }
}