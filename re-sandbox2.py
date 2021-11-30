import re

#   01234567890 123456789
Line ="Dec-01-2021\t1.0 miles\t5.0 min"
SearchStr = '([\d\.]+) miles\t([\d\.]+) min'
Result = re.search(SearchStr, Line)
Result.start()

print(Result.groups())

print("Average speed =", float(Result.group(1))/float(Result.group(2)), " miles/min") 

