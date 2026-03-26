a=input("enter your password:")
up=0
sm=0
dg=0
sp=0
if len(a)>7:
    for i in (a):
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            sm=sm+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    print("the password is strong")
else:
    print("the passwordis very weak")