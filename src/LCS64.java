import java.lang.Math;

class Solution {
    public int minPathSum(int[][] grid) {
        for (int m = 0; m < grid.length; m++) {
            for (int n = 0; n < grid[0].length; n++) {
                if (n == 0 && m == 0) {
                    continue;
                } else if (n == 0) {
                    grid[m][n] += grid[m-1][n];
                } else if (m == 0) {
                    grid[m][n] += grid[m][n-1];
                } else {
                    grid[m][n] += Math.min(grid[m-1][n],grid[m][n-1]);
                }
            }
        }
        return grid[grid.length-1][grid[0].length-1];
    }
}