from itertools import permutations
x = input().split()
x1, x2 = x[0], int(x[1])
l = sorted(list(permutations(x1, x2)))
for i in l:
    print(''.join(i))