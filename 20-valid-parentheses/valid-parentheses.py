class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hMap = {")": "(", "}": "{", "]": "["}
        for paren in s:
            if paren in hMap:
                if stack and stack[-1] == hMap[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        if not stack:
            return True
        return False