# Problem Set 2, hangman.py
# Name: Ben White
# Collaborators: N/A
# Time spent: 3 hrs

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for i in secret_word:
        if i in letters_guessed:
            count += 1
    if count >= len(secret_word):
        return True
    else:
        return False

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = ""
    for i in secret_word:
        if i in letters_guessed:
            word_progress += str(i)
        else:
            word_progress += "*"
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    pos = 0
    for i in range(len(alphabet)):
        if alphabet[pos] in letters_guessed:
            alphabet.pop(pos)
        else:
            pos += 1
    return str(''.join(alphabet))

def with_help_helper(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            letters_guessed.append(i)
            print(f"Letter revealed: {i}")
            return i

def guess_helper(secret_word, letters_guessed, guesses, guess):
    if guess == "!" and with_help == True:
        if guesses > 3:
            guesses -= 3
            guess = with_help_helper(secret_word, letters_guessed)
            return (letters_guessed, guesses)
        else:
            print("You don't have enough guesses! Guess again.")
            return (letters_guessed, guesses)
    elif type(guess) != str or len(guess) > 1 or guess in r" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
        print("Invalid guess! Guess a single letter.")
        return (letters_guessed, guesses)
    else:
        guess = guess.lower()
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter!")
            return (letters_guessed, guesses)
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Correct guess!")
            else:
                print("Try again!")
                if guess in "aeiou":
                    guesses -= 2
                else:
                    guesses -= 1
            return (letters_guessed, guesses)

def score_calculation(guesses, secret_word):
    unique_cha = []
    unique_count = 0
    for i in secret_word:
        if i not in unique_cha:
            unique_cha.append(i)
            unique_count += 1
    total_score = (guesses + (4 * len(unique_cha)) + (3 * len(secret_word)))
    return total_score

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    letters_guessed = []
    play = True
    print(f"The word has {len(secret_word)} characters.")
    while play == True:
        print("-------------------------------------")
        print(f"You have {guesses} guesses remaining.")
        print(f"Avaliable letters: {get_available_letters(letters_guessed)}")
        print(get_word_progress(secret_word, letters_guessed))
        guess = input("Guess a lowercase letter: ")
        (letters_guessed, guesses) = guess_helper(secret_word, letters_guessed, guesses, guess)
        if has_player_won(secret_word, letters_guessed) == True:
            print("You win!")
            print(f"Your total score for this game is: {score_calculation(guesses, secret_word)}")
            play = False
        elif guesses <= 0:
            print(f"You ran out of guesses! The word was {secret_word}")
            play = False






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)
    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print(get_available_letters(letters_guessed))
