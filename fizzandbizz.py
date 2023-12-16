'''
cretae fizz & bizz
'''
from icecream import ic 
def fizz_bizz(n):
    for i in range(1, n + 1):
        result = "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
        ic(result)


if __name__ == "__main__":
    ic.disable()
    ic("hello world")
    ic.enable()
    fizz_bizz(int(input("please enter a number ")))
