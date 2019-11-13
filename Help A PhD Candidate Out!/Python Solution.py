for i in range(int(input())):
    line = input()
    print(eval(line) if "+" in line else "skipped")
