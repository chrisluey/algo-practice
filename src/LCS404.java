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
    public int sumOfLeftLeaves(TreeNode root) {
        int result = 0;
        return leaves(result, root, false);
    }
    
    public int leaves(int num, TreeNode node, boolean bool) {
        if (node == null) {
            return num;
        }
        if (bool) {
            if (node.left == null && node.right == null) {
                return node.val + num;
            } else {
                return leaves(num, node.left, true) + leaves(num, node.right, false);
            }
        } else {
            return leaves(num, node.left, true) + leaves(num, node.right, false);
        }
    } 
}