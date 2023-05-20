n, m = map(int,input().split())
current_sum = 0
all = [x for x in range(n,0,-1)]
counter = 0
already_added = []
while current_sum < m:
    if current_sum + all[counter] > m:
        counter += 1
    else:
        current_sum += all[counter]
        already_added.append(all[counter])
        counter += 1
print(len(already_added))
already_added.reverse()
print(" ".join(str(i) for i in already_added))