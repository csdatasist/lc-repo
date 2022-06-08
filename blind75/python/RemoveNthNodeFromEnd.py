class RemoveNthNodeFromEndofList:
    """
    Desc:
        # 19
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
    Link: 
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    Notes:
    """

    # two pointers, create prehead, iterate right by n, then iterate both until the end to find what needs to be removed
    # Time: O(n)
    # Space: O(1)
    def removeNthFromEnd(self, head, n):
        prehead = ListNode(0, head)
        left, right = prehead, head
        
        # iterate right first n times
        for i in range(n):
            right = right.next 

        # iterate both until right hits end
        while right:
            right = right.next
            left = left.next 

        # remove nth
        left.next = left.next.next 

        return prehead.next 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next