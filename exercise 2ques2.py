var = input("Please enter an integer: ")

if not var.isdecimal():
    print("Invalid integer:", var)
    exit(1)

for var in range(int(var),-1,-2):
    print(var)