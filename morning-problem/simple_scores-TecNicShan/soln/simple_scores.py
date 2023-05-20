num_characters = int(input())
characters = sorted(list(input()))
#print(characters)
counter = 0
for x in (characters):
    if x == "#":
        counter += 1
    if x == "b":
        counter -= 1

if counter == 0:
    print(0)

sharp_list = list("#" for x in range(abs(counter)))
flat_list = list("b" for x in range(abs(counter)))
#print(flat_list)
#print(sharp_list)
#print(counter)
if counter >0:
    print("".join(sharp_list))
if counter <0:
    print("".join(flat_list))

