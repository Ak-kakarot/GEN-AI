import time

a=int(input())
b=input()
for i in range(a):
    print("{}.{}".format(i+1,b))
    time.sleep(2)
