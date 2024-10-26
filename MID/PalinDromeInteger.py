def isPalinDrome(num: int):
   a = 0
   c = num
   
   while num > 0:
      r = num % 10
      num = num // 10
      a = (10 * a) + r
      
   if a == c:
      return True
   else:
      return False

num = int(input("Please input number: "))
print(isPalinDrome(num))