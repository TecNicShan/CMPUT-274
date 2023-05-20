days = int(input())
prices = list(map(int,input().split()))
index = 0
max_diff = 0
min_price = prices[0]
      
for x in range(1, days):
    if prices[x] - min_price > max_diff:
        max_diff = prices[x] - min_price
      
    if prices[x] < min_price:
        min_price = prices[x]
print(max_diff)
