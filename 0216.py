rooms, girls = map(int, input().split(" "))
if(rooms == 0 or girls == 0):
    print(0)
else:
    chance = (100 / (rooms * girls)) / 100

    print("{0:.6f}".format(chance))
