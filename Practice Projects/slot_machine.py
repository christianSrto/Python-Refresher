import random 
import time

icon = ["⛔", "🍒", "🍋", "🍊", "🍉"]
value = [0, 1, 2, 3, 4]

def spin_row():
    return random.choice(value)

def print_row(row1, row2, row3):
    time.sleep(1)
    print(f"| {icon[row1]} |", end="")
    time.sleep(1)
    print(f" {icon[row2]} |", end="")
    time.sleep(1)
    print(f" {icon[row3]} |", end="")


def get_payout(row1, row2, row3, bet):
    if row1 == 0 or row2 == 0  or row3 == 0:
        return 0
    elif row1 == row2 == row3:
        return value[row1] * bet
    elif row1 == row2 or row1 == row3 or row2 == row3:
        return   bet/2
    else: 
        return 0
    

def main():

    balance = 100
    print("----------------------------")
    print("Welcome to the Slot Machine!")

    while balance > 0:
        print(f"Your current balance is: ${balance}")
        
        bet = input("Place your bet ammount or 0 to exit:")
        if bet == "0":
            print(f"Your final balance is: ${balance}")
            print("Thank you for playing! Goodbye!")
            break

        while not bet.isdigit() or int(bet) <= 0 or int(bet) > balance:
            print("Invalid input. Please enter a valid bet amount.")
            bet = input("Place your bet amount:")

        bet = int(bet)
        
        print("Spinning the reels...")
        row1 = spin_row()
        row2 = spin_row()
        row3 = spin_row()

        print_row(row1, row2, row3)
        

        payout = get_payout(row1, row2, row3, bet)
        if payout > 0:
            print(f"You win ${payout}!")
            balance += payout
        else:
            print("You lost.")
            balance -= bet

    print("Gamble responsibly! Your balance is now $0.")



if __name__ == "__main__":
    main()

