/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if(root == null){
            return 0
        }
    var current = root


    // Recursively find the depth of the left and right subtrees
        val leftDepth = maxDepth(root.left)
        val rightDepth = maxDepth(root.right)
        
        // The depth of the current node is 1 plus the maximum of its subtrees
        return maxOf(leftDepth, rightDepth) + 1


    }
}
