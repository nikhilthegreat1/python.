class calculator:

    def __init__(self, num1):
        print(f"the sqaure root of{num1} is {num1*num1}")
        print(f"the cube root of {num1} is {num1*num1*num1}")
        print(f"the square of {num1} is {num1**0.5}")
    @staticmethod
    def hello():
        print("hello world")

a = calculator(4)
a.hello()
