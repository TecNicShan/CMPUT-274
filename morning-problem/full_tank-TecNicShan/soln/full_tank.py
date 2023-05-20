
length, tank, stations, time_to_fill = map(int, input().split())

gas = list(map(int, input().split()))
gas.append(length)
# print(length)
# print(gas)


current = 0
station_num = 0

while current < length:
    for x in range(stations+1):
        # print(current)
        try:
            if current + tank > gas[x] and current + tank >= gas[x+1]:
                continue
        except IndexError:
            x = x-1
        if current + tank >= length:
            current = current + tank
            # print("yes")
        else:
            station_num += 1
            current = gas[x]


time_used = station_num * time_to_fill + length
print(time_used)
