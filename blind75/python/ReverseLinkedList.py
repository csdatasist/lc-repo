class ReverseLinkedList:
    """
    Desc:
        # 206
        Given the head of a singly linked list, reverse the list, and return the reversed list. 
    Link:
        https://leetcode.com/problems/reverse-linked-list/
    Notes:
    """

    # iterative - store prev and current nodes, iterate thur while flipping the pointer till none is left, drawing it out helps 
    # Time: O(n) - n: number of nodes 
    # Space: O(1) - constant 
    def solution1(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp

        return prev 
            


    # recursive -
    # Time: O()
    # Space: O()
    def solution2():
        pass