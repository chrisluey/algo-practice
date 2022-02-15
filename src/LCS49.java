class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for (String str: strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String currSort = new String(chars);
            if (map.get(currSort) == null) {
                List<String> new_list = new ArrayList();
                new_list.add(str);
                map.put(currSort, new_list);
            } else {
                List<String> new_list = map.get(currSort);
                new_list.add(str);
            }
        }
        List<List<String>> result = new ArrayList(map.values());
        return result;
    }
}