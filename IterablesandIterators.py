import itertools
lenght_string=int(input())
string1=input().split()
size=int(input())
x=list(itertools.combinations(string1,size))
list1=[]
for i in x:
        if 'a' in i:
                list1.append(i)
print(f'{len(list1)/len(x):.3f}')