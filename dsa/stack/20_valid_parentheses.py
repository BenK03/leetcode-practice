class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            # if opening
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            # if closing
            else:
                # stack is empty therefore no match
                if len(stack) == 0:
                    return False

                top = stack[-1]

                if char == ')' and top == '(':
                    stack.pop()
                elif char == '}' and top == '{':
                    stack.pop()
                elif char == ']' and top == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False

        # time complexity O(n)

            
            



        