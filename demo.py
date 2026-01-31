from colorama import Fore

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = str(input('Enter operation: '))
def calc():
    if c == '+':
        print(Fore.GREEN + 'Successful:',a + b)
    elif c == '-':
        print(Fore.GREEN + 'Successful:',a - b)
    elif c == '*':
        print(Fore.GREEN + 'Successful:',a * b)
    elif c == '/' and b != 0:
        print(Fore.GREEN + 'Successful:',a / b)
    else:
        print(Fore.RED + 'Invalid operation!')

if __name__ == '__main__':
    calc()
