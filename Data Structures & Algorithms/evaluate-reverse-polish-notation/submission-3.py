class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else: # operand
                first = int(stack.pop())
                second = int(stack.pop())
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(second - first)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(second / first)
                print("First(" + str(first) + ") " + t + " Second(" + str(second) + ") " + " = " + str(stack[-1]))
            print("Stack: ", stack)
        return int(stack[0])




        