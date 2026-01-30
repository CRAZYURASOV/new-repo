def main():
    print("Hello World!")
if __name__ == '__main__':
    main()

a = int(input('enter a number: '))
b = int(input('enter another number: '))

c = str(input('enter oper: '))

def calc():
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a / b)
print(calc())


def hello():
    print('Hello World from Python')
print(hello())