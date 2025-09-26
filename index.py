from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def postOrder(node: TreeNode, res):
            if node is None:
                return 0,0,res

            leftSum, leftNumNodes, leftRes = postOrder(node.left, res)
            rightSum, rightNumNodes, rightRes = postOrder(node.right, res)
            
            numNodes = leftNumNodes + rightNumNodes

            curAvg = (leftSum + rightSum + node.val) // (numNodes + 1)

            res = leftRes + rightRes
            if node.val == curAvg:
                res += 1
            
            return leftSum + rightSum + node.val, numNodes + 1, res
        
        _,_,res = postOrder(root, 0)

        return res
    

if __name__ == "__main__":
    sol = Solution()

    res = sol.averageOfSubtree()