class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if len(stack) == 0:
                stack.append(p)
            elif p == "(" or p == "[" or p == "{":
                stack.append(p)
            elif (p == ")" and stack[-1] == "(") or (p == "]" and stack[-1] == "[") or (p == "}" and stack[-1] == "{"): 
                stack.pop()
            else:
                stack.append(p)
            print(stack)
        return len(stack) == 0
        