from cgitb import small


n_enemies , n_classes = map(int, input().split())
enemy = input().split()
classes = input().split()

enemy = sorted([int(x) for x in enemy],reverse=True)
classes = sorted([int(x) for x in classes],reverse=True)

max_enemy = max(enemy)
smallest_class = 10001


for x in classes:
    if x > max_enemy and x < smallest_class:
        smallest_class = x

if smallest_class == 10001:
    print(-1)
else:
    print(smallest_class)
