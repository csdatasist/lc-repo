class LinkedListCycle:
    """
    Desc:
        # 141
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
    Link: 
        https://leetcode.com/problems/linked-list-cycle/
    Notes:
    """

    # set to check for dups, iterate thru list while checking for dups
    # Time: O(n)
    # Space: O(n)
    def solution1(self, head):
        dups = set()
        curr = head 

        while curr:
            if curr in dups:
                return True
            dups.add(curr)
            curr = curr.next

        return False


    # fast and slow pointers, set slow and fast to head, iterate slow and fast, check if they equal, order matters  
    # Time: O(n)
    # Space: O(1)
    def solution2(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True

        return False