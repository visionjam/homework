import random
random.seed(10000)
n= random.randint(5,10)
for i in range(0,n+1):
    print("{0:^18s}".format(chr(64+i)*(2*i-1)),end="")
    print()
