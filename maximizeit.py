from itertools import product

# Read input
K, M = map(int, input().split())
lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])  # skip the first number (size)

# Cartesian product of all lists
max_val = 0
for combo in product(*lists):
    val = sum(x**2 for x in combo) % M
    max_val = max(max_val, val)

print(max_val)