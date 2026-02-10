import random


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Enter a number")


def play_game():
    print("\nNumber Game")

    low = get_number("Low number: ")
    high = get_number("High number: ")

    if low >= high:
        print("High must be greater")
        return

    attempts = get_number("Attempts: ")
    number = random.randint(low, high)

    for i in range(attempts):
        guess = get_number(f"Guess {i+1}: ")

        if guess == number:
            print("You win!")
            return
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

    print(f"Game over. The number was {number}")


def main():
    name = input("What is your name: ")
    print(f"Hello {name}")

    while True:
        play_game()

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


main()
