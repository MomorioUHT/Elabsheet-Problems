x = int(input("Enter amount of money: "))
origin = x

thousand = x//1000
x%=1000
fiveHundred = x//500
x%=500
hundred = x//100
x%=100
fifty = x//50
x%=50
twenty = x//20
x%=20
ten = x//10
x%=10
five=x//5
x%=5
two=x//2
x%=2
one = x

if (origin >= 1000 and thousand != 0): 
    print(f"1000: {thousand}")
if (origin >= 500 and fiveHundred != 0): 
    print(f"500: {fiveHundred}")
if (origin >= 100 and hundred != 0): 
    print(f"100: {hundred}")
if (origin >= 50 and fifty != 0): 
    print(f"50: {fifty}")
if (origin >= 20 and twenty != 0): 
    print(f"20: {twenty}")
if (origin >= 10 and ten != 0): 
    print(f"10: {ten}")
if (origin >= 5 and five != 0): 
    print(f"5: {five}")
if (origin >= 2 and two != 0): 
    print(f"2: {two}")
if (origin >= 1 and one != 0): 
    print(f"1: {one}")