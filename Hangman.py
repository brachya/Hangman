def color() -> None:
    """
    this will change the color of the printed text
    :return: none
    """
    text = int(
        input(
            "black - 30\nred - 3\ngreen - 32\nyellow - 33\nblue - 34\npurple - 35\ncyan - 36\nwhite - 37\n"
            "Hello which text's color do you want ?"
        )
    )
    background = int(
        input(
            """
    black - 40
    red - 41
    green - 42
    yellow - 43
    blue - 44
    purple - 45
    cyan - 46
    white - 47
    Hello which background color do you want? """
        )
    )
    style = int(
        input(
            """
    1 - normal
    2 - bold
    3 - negative 1
    4 - underline
    5 - negative 2
    Hello which style of text do you want? """
        )
    )
    print(f"\033[{style};{text};{background}m")


def choose_word(file_path: str, index: int) -> str:
    """
    this will take word from file text's that the place of the word singed by number of index
    :param file_path: file text with few word separate by space
    :param index: integer above 0
    :return: the word that has the same place the index number
    """
    with open(file_path, "r") as words_file:
        words = tuple(set(words_file.read().split(" ")))
    return words[index % len(words)]


def print_hangman(num_of_tries: int) -> None:
    """
    printing the state of the player
    :param num_of_tries: number of the mistakes
    :return: none
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def check_win(secret_word: str, old_letters_guessed: list[str]) -> bool:
    """
    this will check from the old letter that the user guessed if it's fill all the letters in secret word
    :param secret_word: string
    :param old_letters_guessed: list of letters
    :return: win or not and if win quit the game
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_words(secret_word: str, old_letters_guessed: list[str]) -> str:
    """
    this will take the letters that the user guessed and show the place of the letters in the mystery word
    :param secret_word: string
    :param old_letters_guessed: list of letters
    :return: the place of the letters in the hidden word
    """
    part_of_the_word: list[str] = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            part_of_the_word.append(letter)
        else:
            part_of_the_word.append("_")
    word = " ".join(part_of_the_word)
    return word


def check_valid_input(letter_guessed: str, old_letters_guessed: list[str]) -> bool:
    """
    this will check the input of the letter if it's okay
    :param letter_guessed: str
    :param old_letters_guessed: list of the letters that has guessed
    :return: none
    """
    letters = (
        "abcdefghijklmnopqrstuvwxyz"  # didn't use .isalpha() because other languages
    )
    return (
        len(letter_guessed) == 1
        and letter_guessed in letters
        and letter_guessed not in old_letters_guessed
    )


def letter_in_word(letter_guessed: str, secret_word: str) -> bool:
    """
    this will check the letter if it's in the secret word
    :param letter_guessed: the letter that has guessed
    :param secret_word: the word that the user trying to find
    :return: boolean
    """
    return letter_guessed in secret_word


def try_update_valid_input(
    letter_guessed: str, old_letters_guessed: list[str], secret_word: str
) -> bool:
    """
    this will filter a letter for the correct options
    :param letter_guessed:string
    :param old_letters_guessed:the list that the user tried
    :param secret_word:the word that has to be found
    :return:boolean
    """
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        if letter_in_word(letter_guessed, secret_word):
            print(show_hidden_words(secret_word, old_letters_guessed))
            return True
        else:
            print(":)\n")
            return False
    else:
        old_letters_guessed.sort()
        print("X" + "\n" + "->".join(old_letters_guessed))
        return True


HANGMAN_ASCII_ART = r"""Welcome to the game Hangman
    _    _
   | |  | |
   | |__| |  __ _ _ ___  __ _ _ __ ____  __ _ _ ___
   |  __  | / _' | '_  | / _' | '_ ' _ | / _' | '_ |
   | |  | || (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_| \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/
"""  # logo of hangman

MAX_TRIES = 6  # max tries of the player
HANGMAN_PHOTOS = {
    0: "",
    1: """
    x-------x
""",
    2: """
    x-------x
    |
    |
    |
    |
    |
""",
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
""",
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
    5: r"""
    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |
""",
    6: r"""
    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |
""",
    7: r"""
    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |""",
}  # levels of the hangman


def hangman_game() -> None:
    """
    this run the game of hangman, and you can run it from the main function
    :return: none
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)
    secret_word = choose_word(
        input("please enter your file path: "),
        int(input("please choose your word's place: ")),
    )
    old_letters_guessed: list[str] = []
    num_of_tries = 1
    print_hangman(num_of_tries)
    print(show_hidden_words(secret_word, old_letters_guessed))
    while num_of_tries != 7:
        if not try_update_valid_input(
            input("Guess a letter: "), old_letters_guessed, secret_word
        ):
            num_of_tries += 1
            print_hangman(num_of_tries)
        check_win(secret_word, old_letters_guessed)
        if num_of_tries == 7:
            print("Lose")
            print("The word is : ", secret_word)
        elif check_win(secret_word, old_letters_guessed):
            print("Win")
            break


def main() -> None:
    """
    this is the main function from here you do or the game or changing the color or exit the game
    :return: none
    """
    answer = input("Play\nColor\nExit\nWrite your choice: ")
    if answer.lower() == "play" or answer.lower() == "p":
        hangman_game()
        main()
    elif answer.lower() == "color" or answer.lower() == "c":
        color()
        main()
    elif answer == "exit" or answer.lower() == "e":
        print("Thank you it was pleasure to play with you!")
    else:
        print("Wrong input!")
        main()


if __name__ == "__main__":
    main()
