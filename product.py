from itertools import product
def product1(a,b):
        return product(a,b)
        
if __name__=='__main__':
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        for pair in product1(a,b):
        