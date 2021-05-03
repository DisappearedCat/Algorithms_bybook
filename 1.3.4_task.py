if __name__ == "__main__":
    stack = []
    input_str = input("Enter string: ")

    for i in input_str:
        ch = ''
        if i == '(' or i == '{' or i == '[':
            stack.append(i)  # if i is a left part of parentheses put it into stack
        else:
            if len(stack) == 0:
                print(False)
                exit()

            ch = stack.pop()  # if i is a right part of parentheses check lef part
            if (ch == '(' and i == ')') or (ch == '{' and i == '}') or (ch == '[' and i == ']'):
                pass
            else:
                print(False)
                exit()

    if len(stack) == 0:
        print(True)
    else:
        print(False)
