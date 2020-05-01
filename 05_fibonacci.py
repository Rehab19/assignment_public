
fib = [1] 
a = 0
b = 1
for i in range(9):
  c = a + b 
  a = b 
  b = c 
  fib.append(b)
print(fib)