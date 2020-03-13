stack = []
a = input().split()
for i in a:
    if i == '+':
        stack.append(stack.pop(-2) + stack.pop(-1))
    elif i == '-':
        stack.append(stack.pop(-2) - stack.pop(-1))
    elif i == '*':
        stack.append(stack.pop(-2) * stack.pop(-1))
    elif i == '/':
        stack.append(stack.pop(-2) // stack.pop(-1))
    elif i == '~':
        stack.append(-stack.pop(-1))
    elif i == '#':
        stack.append(stack[-1])
    elif i == '!':
        num = 1
        for j in range(1, stack.pop(-1) + 1):
            num *= j
        stack.append(num)
    elif i == '@':
        stack.append(stack.pop(-2))
        stack.append(stack.pop(-2))
        stack.append(stack.pop(-3))
    else:
        stack.append(int(i))
print(stack[0])
