def get_result(s):
    stack = []
    num = 0
    result = ''
    for char in s:
        if char == '}':
            str_to_repeat = ''
            while stack[-1] != '{':
                str_to_repeat = stack.pop() + str_to_repeat
            stack.pop()
            repeat = int(stack.pop())
            for i in range(repeat):
                for c in str_to_repeat:
                    stack.append(c)
        elif char.isdigit():
            num = num + int(char)
            stack.append(str(num))
            num = 0
        else:
            stack.append(char)
    while stack:
        result = stack.pop() + result
    return result
print(get_result("ab2{g}3{a2{fg}}"))