cats_count = int(input())
cats_coords = list(map(int, input().split(" ")))

minutes = 0

max_point = max(cats_coords)

min_point = min(cats_coords)

minutes = max_point - min_point

print(minutes)
