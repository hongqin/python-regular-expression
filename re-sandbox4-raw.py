
# why r in front of the string? 

import re

Line1 =r"12\01\2021\t1.0 miles\t5.0 min"
Line2 ="12\01\2021\t1.0 miles\t5.0 min"
print("Line1=\"", Line1, "\"")
print("Line2=\"", Line2, "\"")

mypattern = r"\\"
Result = re.split(mypattern, Line1)
for e in Result: 
  print(e)

print("************************")
Result = re.split(mypattern, Line2)
for e in Result: 
  print(e)

