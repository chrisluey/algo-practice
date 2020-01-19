import java.util.*;

class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        for(int i = 0; i < prices.length - 1; i++)
        {
            int x = prices[i];
            for (int j = i; j < prices.length; j++)
            {
                if (x < prices[j])
                    x = prices[j];
            }
            result = Math.max(x - prices[i], result);
        }
        return result;
    }
}