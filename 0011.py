count = int(input())
cookies = sum(list(map(int, input().split(" "))))
cookies_can_eat = cookies - count

print(cookies_can_eat)
