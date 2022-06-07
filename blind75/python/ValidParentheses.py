class LC:
    """
    Desc:
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        # 20
    Link: 
        https://leetcode.com/problems/valid-parentheses/
    Notes:
    """

    # stack - add to stack if its opening, closing must have match backet on top of stack, check stack is empty at end
    # Time: O() - length of s 
    # Space: O(n) - size of s
    def solution1(self, s):
        closeMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []

        for p in s:
            if p in closeMap:
                if stack and stack[-1] == closeMap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return True if len(stack) == 0 else False 


    # name
    # Time: O()
    # Space: O()
    def solution2():
        pass