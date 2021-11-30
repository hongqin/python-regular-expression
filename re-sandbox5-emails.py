
import re

## Suppose we have a text with many email addresses
str = 'purple alice-smith@google.com, blah monkey bob@abc.com blah dishwasher joe.biden@whitehouse.gov'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)
