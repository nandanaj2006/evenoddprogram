import sys
print("Enter 3 numbers ")
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a>=b and a>=c:
  print(a,"is greater")
elif b>=c and b>=a:
  print(b, "is greater ")
else:
  print(c , "c is greater")
