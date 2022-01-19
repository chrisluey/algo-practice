class Solution {   
    public boolean isValidSudoku(char[][] board) {
        
        List<Set<Character>> subBoxSets = new ArrayList<>();
        for (int d = 0; d < 9; d++) {
            subBoxSets.add(new HashSet<>());
        }
        
        for (int i = 0; i < 9; i++) {
            Set<Character> colSet = new HashSet<>();
            Set<Character> rowSet = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                char curr = board[i][j];
                char reverseCurr = board[j][i];
                if (reverseCurr == '.') {
                    ;;
                } else if (rowSet.contains(reverseCurr)) {
                    return false;
                } else {
                    rowSet.add(reverseCurr);
                }
                if (curr == '.') {
                    ;;
                } else if (colSet.contains(curr)) {
                    return false;
                } else {
                    colSet.add(curr);
                }
                int currSubBox = getSubBox(i,j);
                if (curr == '.') {
                    ;;
                } else if (subBoxSets.get(currSubBox).contains(curr)) {
                    return false;
                } else {
                    subBoxSets.get(currSubBox).add(curr);
                }
            }
        }
        return true;
    }
    
    public int getSubBox(int row, int col) {
        if (row < 3) {
            if (col < 3) {
                return 0;
            } else if (col < 6) {
                return 1;
            } else {
                return 2;
            }
        } else if (row < 6) {
            if (col < 3) {
                return 3;
            } else if (col < 6) {
                return 4;
            } else {
                return 5;
            }
        } else {
            if (col < 3) {
                return 6;
            } else if (col < 6) {
                return 7;
            } else {
                return 8;
            }
        }
    }
}