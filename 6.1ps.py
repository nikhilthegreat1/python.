a1 = int(input("enter no. one"))
a2 = int(input("enter no. two"))
a3 = int(input("enter no. four"))
a4 = int(input("enter no. five"))

if(a1>=a2 and a1>=a4 and a1>=a3):
    print("a1 is greatest no.", a1)
elif(a2>=a1 and a2>=a3 and a2>=a4 ):
    print("a2 is greatest no.", a2)
elif(a3>=a1 and a3>=a2 and a3>=a4 ):
    print("a3 is greatest no.", a3)
elif(a4>=a1 and a4>=a2 and a4>=a3 ):
    print("a4 is greatest no.", a4)
else:
    print("no one is greates")