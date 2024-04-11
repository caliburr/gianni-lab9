"""
Gianni Garcia
"""


def convert(char) -> str:
    char = int(char) + 3
    if char >= 10:
        char -= 10
    return str(char)


def encode(password: str) -> str:
    return ''.join(map(convert,  password))


def decode(password: str) -> str:
    pass


def main() -> None:
    on = True
    while on:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        option = int(input("\nPlease enter an option: "))

        match option:
            case 1:
                encoded = encode(input("Please enter your password to encode: "))
                print("Your password has been encoded and stored!\n")
            case 2:
                print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}")
            case 3:
                on = False
            case _:
                raise ValueError("womp womp weoweoweowoew")


if __name__ == "__main__":
    main()
