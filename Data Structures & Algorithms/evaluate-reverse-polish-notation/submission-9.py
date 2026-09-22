import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        for i in tokens:
            if i in operations:
                op=operations[i]
                first=stack.pop()
                second=stack.pop()
                stack.append(int(op(second,first)))
            else:
                stack.append(int(i))
        return stack[0]
        