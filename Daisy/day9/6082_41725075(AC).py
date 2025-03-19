n =int(input())

for i in range(1, n+1):
  if any(d in "369" for d in str(i)):
    print("X", end=' ')
  else :
    print(i, end=' ')
