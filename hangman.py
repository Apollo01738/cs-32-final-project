import random

def findoccurences(word, ch):
    return [i for i, letter in enumerate(word) if letter == ch]


def hangman2_main():
    # To determine how many coins to award at the end
    won = False

    #To determine if the game is going to be replayed
    replay = False

    print('Welcome to HANGMAN!')

    # set the number of guesses to zero and create empty list to store guesses. have computer choose random word from the list.
    guesses = 0
    correct_guesses = []

    word_list = ['apple', 'banana', 'carrot', 'dinosaur', 'elephant', 'flamingo',
        'giraffe', 'hamburger', 'igloo', 'jungle', 'koala', 'lemon', 'mango',
        'noodle', 'ocean', 'penguin', 'queen', 'rainbow', 'sunflower',
        'turtle', 'cactus', 'butterfly', 'sandwich', 'guitar', 'honey',
        'octopus', 'raincoat', 'eggplant', 'avocado', 'mushroom', 'piano',
        'kiwi', 'dolphin', 'fireworks', 'notebook', 'toucan', 'quilt',
        'ice cream', 'jacket', 'laptop']

    word = random.choice(word_list)

    # print out a blank version of the word with each letter replaced by an underscore
    for letter in word:
        correct_guesses.append('_')
    print(' '.join(correct_guesses))

    while True:
        letter = input("Guess a letter: ")

        # if the letter is in the word, add it to the list of correct guesses
        if letter in word:
            occurrences = findoccurences(word,letter)
            for i in occurrences:
                correct_guesses[i] = letter
                print(' '.join(correct_guesses))
        
    # if the letter is not in the word, increment the number of guesses
        elif letter not in word:
            guesses += 1
            print("Incorrect guess. You have " + str(len(word) - guesses) +
                  " guesses left.")

    # print out the current version of the word with all correct letters revealed
        if '_' not in correct_guesses:
            while True:
                try:
                    print("Congratulations! You guessed the word!")
                    won = True
                    print('1. Play again')
                    print('2. Return to main menu')
                    hangman_option = input('Enter your selection:')
                    if hangman_option == "1":
                        replay = True
                        break
                    elif hangman_option == "2":
                        replay = False
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("Please choose either '1' or '2'.")
            break
            

    # if the number of guesses is exceeded, tell player they lost
        elif guesses == len(word):
            print("Sorry, you didn't guess the word. The word was " + word)
            while True:
                try:
                    print('1. Play again')
                    print('2. Return to main menu')
                    hangman_option = input('Enter your selection:')
                    if hangman_option == "1":
                        replay = True
                        break
                    elif hangman_option == "2":
                        replay = False
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("Please choose either '1' or '2'")
            break
    return won, replay


#if __name__ == '__main__':
    #hangman2_main()
