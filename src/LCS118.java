class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList();
        List<Integer> one = new ArrayList();
        one.add(1);
        list.add(one);
        if (numRows == 1) {    
            return list;
        } else {
            List<Integer> two = new ArrayList();
            two.add(1);
            two.add(1);
            list.add(two);
            if (numRows == 2) {
                return list;
            }
        }
        
        for (int i = 3; i <= numRows; i++) {
            List<Integer> curr = new ArrayList();
            List<Integer> last = list.get(list.size() - 1);
            curr.add(1);
            for (int j = 0; j < last.size() - 1; j++) {
                curr.add(last.get(j) + last.get(j + 1));
            }
            curr.add(1);
            list.add(curr);
        }
        
        return list;
    }
}