class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dict1 = { 
                '*': lambda a, b: a * b,
                '/': lambda a, b: int(a/b) if b!= 0 else "Error division by zero", 
                '+': lambda a, b: a + b, 
                '-': lambda a, b: a - b
                }
        stack = []

        for i in tokens:
            if i in dict1 and len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(dict1[i](a,b))
            else:
                stack.append(int(i))
        return stack.pop()
