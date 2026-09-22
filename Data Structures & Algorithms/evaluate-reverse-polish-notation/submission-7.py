import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+":operator.add,"-":operator.sub,"*":operator.mul,"/": lambda b, a: int(b / a)}
        for i in tokens:
            if i in operations:
                op=operations[i]
                first=stack.pop()
                second=stack.pop()
                stack.append(op(second,first))
            else:
                stack.append(int(i))
        return stack[0]
        