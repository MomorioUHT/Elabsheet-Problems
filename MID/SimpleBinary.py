x = int(input("Enter Binary digits: "))
up,result = 0,0

while (x > 0):
    curr = x%10
    result += curr*(2**up)
    up+=1
    x = x//10 
  
print(result)