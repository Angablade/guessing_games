import random

def main():
    num = random.randint(0,10)
    
    is_correct = False
    while is_correct != True:
        guess = input("Enter a Number between 0 and 10 \n")
        guess = convert_input(guess)
        if (isinstance(guess, int) and guess >=0) == True:
            if guess == num:
                print("Guess is correct!")
                is_correct = True
            elif guess > num:
                print("Guess to big!")
            elif guess < num:
                print("Guess is to little!")
        elif isinstance(guess, int) != True :
            print("Please Enter the a postive integer")

    print(f"Guess: {guess}")
    print(f"Number: {num}")

def convert_input(u_in):

    try:
        u_in = int(u_in)
    except ValueError:
        print("Please enter a Positive integer!")
    
    return u_in
    
main()