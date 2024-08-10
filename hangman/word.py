import random
import json
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


words_fallback = {
    Difficulty.EASY: ["gato", "luz"],
    Difficulty.MEDIUM: ["biscoito", "caneta"],
    Difficulty.HARD: ["morango", "bicicleta"],
}


FILEPATH = "resources/words.json"


def read_valid_difficulty():
    while True:
        print("Escolha a dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        choice = input("Escolha uma opção: ")
        if choice in ["1", "2", "3"]:
            return Difficulty(list(Difficulty)[int(choice) - 1])
        print("Opção inválida, tente novamente.")


def find_random_word(difficulty: Difficulty) -> str:
    try:
        with open(FILEPATH, "r", encoding="utf-8") as file:
            dados = json.load(file)
        return random.choice(dados.get(difficulty.value))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Failed to read JSON file, using in memory fallback: {e}")
        return random.choice(words_fallback[difficulty])
