class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        int acc = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            if (curr == null) {
                continue;
            } else if (curr.val >= low && curr.val <= high) {
                acc += curr.val;
                queue.add(curr.left);
                queue.add(curr.right);
            } else if (curr.val >= low) {
                queue.add(curr.left);
            } else if (curr.val <= high) {
                queue.add(curr.right);
            } else {
                continue;
            }
        }
        return acc;
    }
}