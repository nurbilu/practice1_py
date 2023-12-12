'''
cretae fizz & bizz
'''

def fizz_bizz(n):
    for i in range(1, n + 1):
        result = "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
        print(result)

fizz_bizz(int(input("please enter a number")))
