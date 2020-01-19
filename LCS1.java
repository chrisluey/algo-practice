import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Arrays.sort(nums); 
        int i = 0;
        int j = 1;
        int[] result = new int[2];
        while (i < nums.length - 2 && j < nums.length - 1) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
            } else if (nums[i] + nums[j] < target) {
                if (j == nums.length - 1) {
                    i = i + 1;
                    j = i + 1;
                } else {
                    j = j + 1;
                }
            } else {
                i = i + 1;
                j = i + 1;
            }
        }
        return result;
    }
}