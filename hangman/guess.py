# `all` is similar to `Array.every` in JavaScript, returns true if
#  the specified criteria is valid for all elements
def check_guesses(word, guesses):
    # word is being passed as the iterable array, letter is
    # the current element in the array, and `letter in guesses`
    # is the condition that must be true for all elements
    return all(letter in guesses for letter in word)


def has_guessed_already(guess, previous_guesses):
    return guess in previous_guesses


def read_guess():
    while True:
        guess = input("Adivinhe uma letra: ").strip()
        if len(guess) != 1:
            print("Insira apenas uma letra.")
        elif not guess.isalpha():
            print("O input deve ser uma letra do alfabeto.")
        else:
            return guess


def read_valid_guess(previous_guesses):
    guess = read_guess()
    while has_guessed_already(guess, previous_guesses):
        print("Você já adivinhou essa letra.")
        guess = read_guess()

    return guess
