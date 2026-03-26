import random
name1 = input("player 1:")
name2 = input("player 2:")
d1 = random.randint(1,10)
d2 = random.randint(1,10)
s1 = 25
s2 = 25


print("--player 1--")
while True:
    g=int(input("enter your guess:"))
    if(d1==g):
        print("you guessed correctly")
        break
    elif(d1>g):
        print("your guess is low")
    else:
        print("your guess is higher")
    s1=s1-1
    
print("--player 2--")

while True:
    g=int(input("enter your guess:"))
    if(d2==g):
        print("you guessed correctly")
        break
    elif(d2>g):
        print("your guess is low")
    else:
        print("your guess is higher")
    s2=s2-1
    
if(s1>s2):
    print("player 1 won")
elif(s1<s2):
    print("player 2 won")
else:
    print("draw")
