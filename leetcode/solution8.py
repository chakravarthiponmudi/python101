# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        n = self.getSize(head)
        root = self.recur(head,n)
        return root
    
    def getSize(self,h):
        count = 1
        while h.next != None:
            count +=1
            h = h.next
        
        return count
    
    def recur(self, node, n):
        if n == 0:
            return None
        if n==1:
            return TreeNode(node.val)

        mp = None
        if n%2 == 0:
            mp = n//2
        else:
            mp = n//2 + 1
        root = self.getNodeAt(node, mp)
        left = self.recur(node, mp-1)
        right = self.recur(root.next, n-mp)
        treeRoot = TreeNode(root.val,left,right)
        return treeRoot
    
    def getNodeAt(self, n, i):
        while i >1:
            n = n.next
            i -=1
        return n
        
        
def buildListNode(n):
    h = ListNode()
    r = h
    for i in range(1,n):
        l = ListNode(i)
        h.next = l
        h = l
    return r.next

nodes = buildListNode(20000)
s = Solution()
tree = s.sortedListToBST(nodes)
print(tree)