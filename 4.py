friends = ["nikhil", "appple", 66, False]
print(friends[0])
friends[0] = "grapes" #unlike strings, lists are mutable
print(friends[0])
friends.append("hello")
print(friends)
friends.reverse()
print(friends)
friends.insert(2,"hellllllo")
print(friends)
friends.pop(2)
print(friends)