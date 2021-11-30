import re

#   01234567890 123456789
Line ="IP address is 1.2.3.4 Not 5.6.7 or 8.9.10.11.12"
SearchStr = "\d*\.*\d+\.\d+\.\d+"
Result = re.search(SearchStr, Line)
print(Result.group())

Line ="IP address is 11.22.33.44 Not 5.6.7 or 8.9.10.11.12"
SearchStr = '\d+\.\d+\.\d+\.\d+'
Result = re.search(SearchStr, Line)
print(Result.group())

