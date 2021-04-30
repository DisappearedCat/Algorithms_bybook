import FixedCapacityStackOfString

if __name__ == "__main__":
    stack = FixedCapacityStackOfString.FixedCapacityStackOfString(10)
    while True:
        inp = input()
        if inp == "-":
            print(stack.pop())
        else:
            stack.push(inp)
