import random
import time

# create a tuple for all symble
symbles = ("🍉","🔔","🍎","✨","😎")

# Functions
def spin_row():
    return [random.choice(symbles) for _ in range(3)] # retrun a list with random symbles

def print_row(row):
    print("\n Spning...")
    time.sleep(2) # hold in 2 sec
    print("---------------------------------------------------")
    print(" | ".join(row))
    print("---------------------------------------------------")

def bet(blance = 100):
    while True:
        amount = input("Enter Your Beting Amount: ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > blance:
                print("\tYou not have this mutch blance!")
                continue
            elif amount < 5:
                if amount < 0:
                    print(f"\t₹{amount} this is not a valid amount amount must be getter then ₹0")
                    continue
                else:
                    print("\tyour amount must be getter then ₹5")
                    continue
            else:
                return amount

def check_wining(name,row,amount):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍉":
            amount = amount * 2
            print(f"\nYou Win {name} your Amount has bin 2x {amount}")
            return amount
        elif row[0] == "🍎":
            amount = amount * 3
            print(f"\nYou Win {name} your Amount has bin 3x {amount}")
            return amount
        elif row[0] == "🔔":
            amount = amount * 4
            print(f"\nYou Win {name} your Amount has bin 4x {amount}")
            return amount
        elif row[0] == "✨":
            amount = amount * 5
            print(f"\nYou Win {name} your Amount has bin 5x {amount}")
            return amount
        elif row[0] == "😎":
            amount = amount * 10
            print(f"\nYou Win {name} your Amount has bin 10x {amount}")
            return amount
    else:
        print(f"You Lose {name} Sorry 🙏 please try again")
        return 0
# main function 
def main():
    blance = 100
    name = input("Enter Your Name: ")
    print("---------------------------------------------------")
    print(f"Wellcome {name} in lucy Spin Game")
    print("""
    Rule:-
    1. you have to bet minimun ₹5
    2. Your Blance is : ₹100
    3. if your blance less then ₹10 then game is over
                thanks for chosing us
    """)
    while blance >= 5:
        ask = input(f"{name} you want to Spin (y/n): ")
        if ask.lower() == "y":
            print("\n---------------------------------------------------")
            amount = bet(blance)
            blance -= amount
            row = spin_row()
            print_row(row)
            wining = check_wining(name,row,amount)
            blance += wining
            print(f"{name} your Blance is: ₹{blance}")
        else:
            break

    print("\n***** Thanks For Playing *****")


if __name__ == "__main__":
    main()
