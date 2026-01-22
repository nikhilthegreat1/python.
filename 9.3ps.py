

def replace(word):
    with open("9.3.txt", "r")as f:
        content = f.read()
        contentnew = content.replace(word, "######")
        with open("9.3.txt","w") as f:
            f.write(contentnew)
replace("donkey")
replace("is")