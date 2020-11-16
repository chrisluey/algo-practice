/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList();
        generateLevelOrder(list, root, 0);
        return list;
    }
    
    public void generateLevelOrder(List<List<Integer>> list, TreeNode node, int lvl) {
        if (node == null) {
            return;
        }
        if (list.size() - 1 < lvl) {
            List<Integer> listEntry = new ArrayList();
            listEntry.add(node.val);
            list.add(listEntry);
        } else {
            list.get(lvl).add(node.val);
        }
        generateLevelOrder(list, node.left, lvl + 1);
        generateLevelOrder(list, node.right, lvl + 1);
    }
}