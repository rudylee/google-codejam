import sys

totalCases = 0
length = 0
lists = []

for line in sys.stdin:
    if 'q' == line.rstrip():
        break

    if totalCases == 0:
        totalCases = int(line)
    else:
        if length == 0:
            length = int(line)
        else:
            lists.append([int(x) for x in line.split(" ")])
            length = 0

total = 0
answer = 1

for x in lists:
    for i in range(0, len(x) - 1):
        minimum = None
        minIndex = -1

        for j in range(i, len(x)):
            if minimum == None:
                minimum = x[j]
                minIndex = j
            elif x[j] < minimum:
                minimum = x[j]
                minIndex = j

        # reverse the list
        x[i:minIndex + 1] = reversed(x[i:minIndex + 1])

        total += ((minIndex - i) + 1)

    print(f'Case #{answer}: {total}')
    total = 0
    answer += 1
