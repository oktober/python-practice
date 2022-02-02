import random
import string

# update to point to a wordlist file
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # take all unique letters in secret_word and put them in a list to iterate over
    unique = list(set(secret_word))

    for letter in unique:
        # if any letter is not in letters_guessed, then the word has not been guessed yet
        if letter not in letters_guessed:
            return False

    return True  


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    wordAsList = list(secret_word)
    hiddenWord = ''

    for letter in wordAsList:
        # if the letter hasn't been guessed yet
        if letter not in letters_guessed:
            # replace it with a '_'
            letter = '_'
        # reconstruct the word with the hidden characters
        hiddenWord += letter + ' '

    return hiddenWord


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    allLetters = list(string.ascii_lowercase)
    notGuessed = ''

    for letter in allLetters:
        if letter in letters_guessed:
            letter = ''
        notGuessed += letter

    return notGuessed


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 6
    warnings = 3
    letters_guessed = []
    uniqueLettersInWord = list(set(secret_word))
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is ", len(secret_word), " letters long.")
    print("You have ", warnings, " warnings left.")
    # must be alpha. If not, reduce their warnings count and display a warning.
        # if warnings count hits zero, then reduce their guesses
    while True:
        print("-----------------------")
        print("You have ", guessesLeft, " guesses left")
        print("Available letters: ", get_available_letters(letters_guessed))
        guess = str(raw_input("Please guess a letter: "))

        if str.isalpha(guess):
            #if the letter is in the uniqueLettersInWord list
            lowercaseGuess = str.lower(guess)
            if lowercaseGuess in letters_guessed:
                # substract a warning
                warnings -= 1
                if warnings > 0:
                    print("Oops! You've already guessed that letter. You have ", warnings, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
                else:
                    guessesLeft -= 1
                    if guessesLeft <= 0:
                        print("Sorry, you ran out of guesses. The word was ", secret_word)
                        break
                    else:
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                letters_guessed += lowercaseGuess

                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations, you won!")
                    print("Your total score for this game is: ", guessesLeft * len(uniqueLettersInWord))
                    break
                elif lowercaseGuess in uniqueLettersInWord:
                    print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                    continue
                else:
                    # add logic so vowels guessed lose 2 guesses
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))

                    if lowercaseGuess in vowels:
                        guessesLeft -= 2
                    else:
                        guessesLeft -= 1

                    if guessesLeft <= 0:
                        print("Sorry, you ran out of guesses. The word was ", secret_word)
                        break
                    
                    continue
        else:
            # substract a warning
            warnings -= 1
            if warnings >= 0:
                print("Oops! That is not a valid letter. You have ", warnings, " warnings left.")
            else:
                guessesLeft -= 1
                if guessesLeft <= 0:
                    print("Sorry, you ran out of guesses. The word was ", secret_word)
                    break
            continue



# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.strip()
    other_word = other_word.strip()

    if my_word == other_word:
        return True

    if len(my_word) == len(other_word):
        uniqueLetters = list(set(my_word.replace("_", "")))

        for i in range(0, len(my_word)):
            if my_word[i] == '_' and other_word[i] in uniqueLetters:
                return False
            elif my_word[i] != '_' and my_word[i] != other_word[i]:
                return False
        return True

    return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = my_word.strip().replace(" ", "")
    uniqueLetters = list(set(my_word.replace("_", "")))
    matchingList = []

    for word in wordlist:
        if len(my_word) == len(word):
            
            addWord = False
            for i in range(0, len(word)):

                if my_word[i] == word[i]:
                    pass
                elif my_word[i] == '_' and word[i] not in uniqueLetters:
                    pass
                else:
                    addWord = False
                    break

                addWord = True
            
            if addWord:
                matchingList.append(word)


    return matchingList


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''    
    guessesLeft = 6
    warnings = 3
    letters_guessed = []
    uniqueLettersInWord = list(set(secret_word))
    vowels = ['a', 'e', 'i', 'o', 'u']

    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is ", len(secret_word), " letters long.")
    print("You have ", warnings, " warnings left.")
    # must be alpha. If not, reduce their warnings count and display a warning.
        # if warnings count hits zero, then reduce their guesses
    while True:
        print("-----------------------")
        print("You have ", guessesLeft, " guesses left")
        print("Available letters: ", get_available_letters(letters_guessed))
        guess = str(raw_input("Please guess a letter: "))

        if str.isalpha(guess):
            #if the letter is in the uniqueLettersInWord list
            lowercaseGuess = str.lower(guess)
            if lowercaseGuess in letters_guessed:
                # substract a warning
                warnings -= 1
                if warnings > 0:
                    print("Oops! You've already guessed that letter. You have ", warnings, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
                else:
                    guessesLeft -= 1
                    if guessesLeft <= 0:
                        print("Sorry, you ran out of guesses. The word was ", secret_word)
                        break
                    else:
                        print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                letters_guessed += lowercaseGuess

                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations, you won!")
                    print("Your total score for this game is: ", guessesLeft * len(uniqueLettersInWord))
                    break
                elif lowercaseGuess in uniqueLettersInWord:
                    print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                    continue
                else:
                    # add logic so vowels guessed lose 2 guesses
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))

                    if lowercaseGuess in vowels:
                        guessesLeft -= 2
                    else:
                        guessesLeft -= 1

                    if guessesLeft <= 0:
                        print("Sorry, you ran out of guesses. The word was ", secret_word)
                        break
                    
                    continue
        elif guess == '*':
            print("Possible word matches are: ")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            continue
        else:
            # substract a warning
            warnings -= 1
            if warnings >= 0:
                print("Oops! That is not a valid letter. You have ", warnings, " warnings left.")
            else:
                guessesLeft -= 1
                if guessesLeft <= 0:
                    print("Sorry, you ran out of guesses. The word was ", secret_word)
                    break
            continue


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
