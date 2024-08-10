import os


# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def draw_word(word, guesses):
    # `join` is concatenating the elements of the array into a string
    # for each letter in word, if the letter is in guesses, return the letter
    # otherwise return an underscore
    return "".join([letter if letter in guesses else "_" for letter in word])
