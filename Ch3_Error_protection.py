import sys
print(sys.executable)


def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(2))
print(spam(11))
print(spam(11.0))
print(spam(0))
print(spam(8))
print(spam(2.5))
