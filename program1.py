import os
num = int(os.environ["NUMBER"])
if num % 2 == 0:
  print(num,"is Even")
else:
  print(num, "is Odd")
