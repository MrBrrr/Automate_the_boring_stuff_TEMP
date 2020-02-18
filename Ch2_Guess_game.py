import random
secret_number = random.randint(1, 30)

for guess_number in range(10):
    print('Take a guess')
    guess = int(input())
    if guess > secret_number:
        print('To high, try again')
    elif guess < secret_number:
        print('To low, try again')
    else:
        break
    
if guess == secret_number:
    print('Great! You guessed in ' + str(guess_number+1) + ' tries')
else:
    print('Secret number was: ' + str(secret_number) + '. Try your luck next time')

