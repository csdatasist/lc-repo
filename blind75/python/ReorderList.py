class ReorderList:
    """
    Desc:
        # 143
        Reorder list as L0, Ln, L1, Ln-1, L2, Ln-2... in place 
    Link: 
        https://leetcode.com/problems/reorder-list/
    Notes:
    """

    # find mid point, split list, reverse second half, merge both halfs 
    # Time: O(n)
    # Space: O(1)
    def reorderList(self, head):
        # find mid point, slow ends as mid point 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        # split the list
        curr = slow.next
        slow.next = None
        
        # reverse second half, prev ends as second start
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # merge 
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next 
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

