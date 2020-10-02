import java.util.Arrays;

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) {
            return false;
        }
        if (matrix[0].length == 0) {
            return false;
        }
        int targetRow = 0;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][matrix[0].length - 1] == target) {
                return true;
            } else if (matrix[i][matrix[0].length - 1] > target) {
                targetRow = i;
                break;
            }
        }
        System.out.println(targetRow);
        if (Arrays.binarySearch(matrix[targetRow], target) >= 0) {
            return true;
        } else {
            return false;
        }
    }
}