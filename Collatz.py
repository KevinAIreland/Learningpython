import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter Number:')

try:
    num=int(input())
except ValueError:
    print ('Please enter an integer')
    sys.exit()
while num != 1:
    num = (collatz(num))
    print(num)

