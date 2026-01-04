age = int(input("enter you age"))

if(age>18):
    print("you can vote")
elif(age == 18):
    print("you can give your first vote")
elif(age < 0):
    print("wrong input")
else:
    print("youy can't vote")