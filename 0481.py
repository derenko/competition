count = list(map(int, input().split(" ")))

if(count[0] + count[1] > count[2]):
    print("YES")
else:
    print("NO")
