from itertools import combinations
x = input().split()
x1, x2 = sorted(x[0]), int(x[1])
l1 = [list(combinations(x1, i+1)) for i in range(x2)]
l2 = [item for sublist in l1 for item in sublist]
for i in l2:
    print(''.join(i))
