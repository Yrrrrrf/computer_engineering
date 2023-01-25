import random

def run():
    print("Guess the number!")
    random_number = random.randint(1, 100)
    guessed_number = int(input("Enter a number:"))
    lives = 5

    while random_number != guessed_number:
        if random_number < guessed_number: 
            print("Select an smaller number.")
            lives -= 1
        elif random_number > guessed_number: 
            print("Select a bigger number.")
            lives -= 1
        if lives == 0:
            print(f"Number was: {random_number}\nYou lost!")
            break
        print("You have {lives} lives left.")
        guessed_number = int(input("Enter a number:"))
    if random_number == guessed_number: 
        print("Congratulations! You won!")


if __name__ == "__main__":
    run()

new_game = "y"
while new_game == "y":
    new_game = input("Wanna play again?    y/n")
    if new_game == "y":
        run()
    elif new_game == "n":
        print("Goodbye!")
    else:
        print("Invalid input!")
