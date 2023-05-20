n, m, k = map(int, input().split())
movies = []
for x in range(n):
    movies.append(list(map(int, input().split())))
scare, watched = 0, 0
sorted_compare = []
for index in range(m):
    compare = [x[index] for x in movies]
    sorted_compare.append(sorted(compare))
sorted_compare = sorted(sorted_compare)
for x in sorted_compare:
    if scare + x[0] <= k:
        scare += x[0]
        watched += 1
print(watched)
