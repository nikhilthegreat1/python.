m1 = int(input("enter marks one"))
m2 = int(input("enter marks two"))
m3 = int(input("enter marks three"))

percentage=100*(m1+m2+m3)/300

if(percentage>=40):
    print("you are passed", percentage)
else:
    print("you failed", percentage)