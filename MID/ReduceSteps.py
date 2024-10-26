x = int(input("Please input number: "))
print(x)
    
steps = 0

while (x > 0):
    if (x % 2 == 0):
        x = int(x/2)
    else:
        x = x-1
    steps += 1
    print(x)

if (steps == 1):
    print("1 step")
else:
    print(f"{steps} steps")