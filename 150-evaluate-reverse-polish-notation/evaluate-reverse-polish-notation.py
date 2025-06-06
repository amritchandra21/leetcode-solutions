class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ["+", "-", "/", "*"]
        def apply_op(op, a, b):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return int(a / b)
        for token in tokens:
            if token in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                comp = apply_op(token, num1, num2)
                stack.append(comp)
            else:
                stack.append(int(token))
        
        return stack.pop()