
start = input()
end = input()
listA = list(input());

def sortedArrayToBST_helper(listA, start, end):

    if start > end:
        return null

    mid = start + (end - start)/2

    TreeNode root = new TreeNode(listA[mid])
    // Recursively construct the left subtree
    // and make it left child of root


    root.left = sortedArrayToBST_helper(A, start, mid - 1)
    // Recursively construct the right subtree
    // and make it right child of root
    root.right = sortedArrayToBST_helper(A, mid + 1, end)
    return root


TreeNode sortedArrayToBST(int A[], int n):
    TreeNode root = sortedArrayToBST_helper(A, 0, n)
    return root
