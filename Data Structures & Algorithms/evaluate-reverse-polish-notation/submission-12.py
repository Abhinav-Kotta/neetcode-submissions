class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                element1, element2 = int(stack.pop()), int(stack.pop())
                stack.append(element1 + element2)
            elif token == '-':
                element1, element2 = int(stack.pop()), int(stack.pop())
                stack.append(element2 - element1)
            elif token == '*':
                element1, element2 = int(stack.pop()), int(stack.pop())
                stack.append(element1 * element2)
            elif token == '/':
                element1, element2 = int(stack.pop()), int(stack.pop())
                print(element1, element2)
                stack.append(int(element2) / element1)
            else:
                stack.append(token)

        return int(stack[-1])