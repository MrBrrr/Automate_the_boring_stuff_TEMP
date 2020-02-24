#! python


def main():
    user_number = None
    while user_number is None:
        print('Enter a number')
        user_number = get_user_number()

    user_number = collatz(user_number)
    while 1 != user_number:
        user_number = collatz(user_number)


def collatz(number):
    
    if 0 == number % 2:       #even
        number = number // 2
    
    else:                   # odd
        number = 3 * number + 1
        
    print(str(number))
    return number


def get_user_number():
    try:
        return int(input())
    except ValueError:
        print('Error: Typed non integer string')


if __name__ == '__main__': main()
