import re

count = int(input())
PHRASE = input()

result = re.findall("TOILET", PHRASE)

if(len(result) == count):
    print("YES")
else:
    print("NO")
