n = (int(input('Enter how many Star you want to print: ')))
flag = (int(input('Enter 0 or 1: ')))
new = bool(flag)
if new == True:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end='')
        print()
elif new == False:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print('*', end='')
        print()
