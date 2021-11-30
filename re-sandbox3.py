
import re

#   01234567890 123456789
Line ="Dec-01-2021\t1.0 miles\t5.0 min"
SearchStr = r'\d+'
Result = re.findall(SearchStr, Line)

print(Result)


