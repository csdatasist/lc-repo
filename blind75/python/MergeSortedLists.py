class MergeTwoSortedLists:
    """
    Desc:
        # 21
        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Link: 
        https://leetcode.com/problems/merge-two-sorted-lists/
    Notes:
    """

    # recursive
    # Time: O(n+m)
    # Space: O(n+m)
    def solution1():
        pass


    # iterative - create start node, go thur lists ordering values
    # Time: O(n+m), n = list1 nodes, m = list2 nodes 
    # Space: O(1)
    def solution2():
        prehead = ListNode()
        curr = prehead
        
        # order the lists until one is empty
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next  
            curr = curr.next
            
            
        # append non empty list at end
        if list1:
            curr.next = list1 
        else: 
            curr.next = list2
        
        return prehead.next 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next