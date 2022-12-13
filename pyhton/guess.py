import random
from word import words
import string 
def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. You are to low')
        elif guess > random_number:
            print('Sorry, guess again. You are to high')
    print(f'Yessay, congrats. you have guessed the right number that is {random_number}')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f'Is {guess} to high (H), too low (L), correct (C)??').lower()
        if feedback == 'h':
             high = guess - 1
        elif feedback == 'l':
            low = guess + 1      
    print(f'yessay the computer have guess your number, {guess}, correctly ! ')


def play():
    user = input("what your choice ?'r' for rock, 's' for scissor, 'p' for paper\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won! '
    
    return 'You lost'
    

def is_win(player, opps):
    if (player == 'r' and opps =='s' ) or (player == 's' and opps == 'p') or (player == 'p' and opps == 'r '):
        return True 
    
def right_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()