LengthOfSquare = int(input("Enter the size of the pattern: "))

iterator = 1
ast = "*"
while iterator <= LengthOfSquare:
 for i in range(0,LengthOfSquare+1):
  if i == LengthOfSquare:
   print(ast*i)
 iterator += 1
