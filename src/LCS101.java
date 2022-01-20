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
    public boolean isSymmetric(TreeNode root) {
        List<TreeNode> queue1 = new ArrayList<>();
        List<TreeNode> queue2 = new ArrayList<>();
        queue1.add(root.left);
        queue2.add(root.right);
        while (!queue1.isEmpty() || !queue2.isEmpty()) {
            TreeNode curr1 = queue1.get(0);
            TreeNode curr2 = queue2.get(0);
            if (curr1 == null ^ curr2 == null) {
                return false;
            } else if (curr1 == null && curr2 == null) {
                ;;
            } else if (curr1.val == curr2.val) {
                queue1.add(curr1.left);
                queue1.add(curr1.right);
                queue2.add(curr2.right);
                queue2.add(curr2.left);
            } else {
                return false;
            }
            queue1.remove(0);
            queue2.remove(0);
        }
        return true;
    }
}