class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in operations:
                first = stack.pop()
                second = stack.pop()

                stack.append(operations[i](second, first))
            else:
                stack.append(int(i))

        return stack[0]