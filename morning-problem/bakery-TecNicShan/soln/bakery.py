n, m, k = map(int, input().split())
n_list = sorted(list(map(int, input().split())), reverse=True)
time = 0
acceptable = 2*k

while len(n_list) > 0:
    start_temp = n_list[-1]
    end_temp = n_list[-1] + acceptable
    try:
        for x in range(m):
            if start_temp <= n_list[-1] <= end_temp:
                n_list.pop()
    except:
        time += 1
        break
    time += 1
print(time)
