import random

WORDS = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

print('Welcome to Word Gussing Game!')

name = input('What\'s your name? ')
print(f'Good luck! {name}')

word = random.choice(WORDS)

print('Guess the characters.')

guesses = ''
turn = 12


while turn > 0:
    failed = 0

    for i in word:
        if i in guesses:
            print(i,end=" ")
        else:
            print('_',end=" ")
            failed +=1

    if failed == 0 :
        print()
        print('You won!')
        print(f'The word is : {word}')
        break
    
    print()
    guess =input('guess a character: ')
    guesses += guess

    if guess not in word:
        turn -= 1
        print('Wrong!')
        print(f'You have {turn} more guesses.')

    if turn == 0:
        print('You loose')