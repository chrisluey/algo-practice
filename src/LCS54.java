class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int top = 0, left = 0, m = matrix.length - 1, n = matrix[0].length - 1;
        while (top <= m && left <= n) {
            for (int i = left; i <= n; i++) {
                result.add(matrix[top][i]);
            }
            top += 1;
            
            for (int i = top; i <= m; i++) {
                result.add(matrix[i][n]);
            }
            n -= 1;
            
            if (top <= m) {
                for (int i = n; i >= left; i--) {
                    result.add(matrix[m][i]);
                }
            }
    
            m -= 1;
            
            if (left <= n) {
                for (int i = m; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
            }
            
            left += 1;
            
        }
        return result;
    }
}