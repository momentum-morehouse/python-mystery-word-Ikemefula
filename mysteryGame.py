# computer ask user to guess 
import random 
file_object = open('words.txt', 'r')
words_list = file_object.readlines()
# print("random item from list is:", random.choice(words_list))
def computer_guess():
    new_word = (random.choice(words_list))
    print(new_word)
    return new_word

def say_hello(word):
    if len(word) > 4:
        print("Hello", word)
    else:
        print("Not Valid")
say_hello(computer_guess())
def guess():
    guess = input("Enter Guess Here")
    return guess 
# confirm correct or incorrect answer
def validate(guess, word):
    if guess in word:
        print("yes")

computer_guess()


# LOOK UP "HOW TO READ A TEXT FILE"


# user loses try on incorrect entry. 
# end game if correct info is there
# end if user runs out of turns





#                   nice to have 
# computer selects 1 random word at a time 
# User selects the level of difficulty 
# computer lets user know how many letters computer's words has
# display partially correct answer  
# remind user of how many tries. possibly a counter. user is allowed 8 tries 
# print message "You've Guessed this twice" if user guesses same letter twice, no turn is taken



