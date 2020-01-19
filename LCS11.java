class Solution {
    public int maxArea(int[] height) {
        int result = 0;
        for (int i = 0; i < height.length; i++)
        {
            for (int j = i; j < height.length; j++)
            {
                int h = Math.min(height[i], height[j]);
                int w = j - i;
                result = Math.max(h * w, result);
            }
        }
        return result;
    }
}