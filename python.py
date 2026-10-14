import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
                    print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and " + str(MAX_LINES) + ".")
        else:
                    print("please enter a number")
    return lines

def get_bet():
    while True:
        bet = input("Enter the bet amount ($" + str(MIN_BET) + " - $" + str(MAX_BET) + ")? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet amount must be between $" + str(MIN_BET) + " and $" + str(MAX_BET) + ".")
        else:
            print("please enter a number")
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount. Your current balance is: ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is: ${bet * lines}.")
    print(balance,lines,bet)

main()