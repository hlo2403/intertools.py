from itertools import combinations_with_replacement
# Input format: "STRING K"
s, k = input().split()
k = int(k)

# Generate combinations and print them
for combo in combinations_with_replacement(sorted(s), k):
    print(''.join(combo))