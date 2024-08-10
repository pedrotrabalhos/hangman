from console import clear_console, draw_word
from guess import read_valid_guess, check_guesses
from word import find_random_word, read_valid_difficulty


def start_game():
    # Game state
    guesses = []
    game_over = False
    max_attempts = 6

    # Presentation
    clear_console()
    print("Bem-vindo ao jogo da forca!")
    print("Vou pensar em uma palavra e você deve adivinhar as letras.")

    difficulty = read_valid_difficulty()
    word = find_random_word(difficulty)

    # Game loop
    while not game_over:
        print(f"🤔 Você tem {max_attempts - len(guesses)} tentativas.")
        print(draw_word(word, guesses))
        guess = read_valid_guess(guesses)
        guesses.append(guess)
        if check_guesses(word, guesses):
            print(f"🎉 You win! a palavra era {word}")
            game_over = True
            continue
        if len(guesses) == max_attempts:
            print(f"🫠 You lose! a palavra era {word}")
            game_over = True
            continue

        clear_console()


if __name__ == "__main__":
    start_game()
