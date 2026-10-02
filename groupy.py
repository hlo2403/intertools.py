from itertools import groupby

# Input
s = input().strip()

# Process and output
for char, group in groupby(s):
    count = len(list(group))
    print(f"({count}, {char})", end=" ")