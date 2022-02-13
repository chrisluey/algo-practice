class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> matrix2(matrix);
        int n = matrix.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = matrix2[n - j - 1][i];
            }
        }
    }
};