num_applicants = int(input())
applicants = []
for x in range(num_applicants):
    applicants.append(int(input()))
applicants.sort(reverse=True)
# print(applicants)
index = 0
while index <= len(applicants)-1:
    if applicants[index] >= index+1:
        index += 1
    else:
        break
print(index)
