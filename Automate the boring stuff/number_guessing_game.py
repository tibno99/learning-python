import random

print('Give me your name')
name = input()
print('Hello ' + name + ' get ready to lose')
secret_number = random.randint(1,1000)
print('DEBUG number is:' + str(secret_number))

for guesses in range(1,5):

    print('Give me a number')
    guess = int(input())

    if guess < secret_number:
        print ('Too low')

    elif guess > secret_number:
        print ('Too high')

    else: break

if guess == secret_number:
    print ('How the hell did you guess ' + str(secret_number) + ' in ' + str(guesses) +' guesses?')

else:
    print(name + ' you are dumb')
        


    

