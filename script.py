import random

money = 100

#Write your game of chance functions here

def get_bet(money):   #for having an external input from the user
  bet = None
  while bet is None:
      try:
          bet = int(input("How much would you like to bet? Enter a whole number only: "))
          while bet > money:
            print("You don't have enough. You only have $" + str(money))
            bet = int(input("How much would you like to bet? Enter a whole number only: "))
          return bet
      except:
          print("Invalid entry.")

def update_cash(money, bet, result):
    if result == True:
        winnings = money + bet
        print("You won. You now have $" + str(winnings) + ".\n") 
        return winnings
    else:
        loss = money - bet
        print("You lost. You now have $" + str(loss) + ".\n")
        return loss
    
def coin_flip(prediction):
  binary_flip = random.randint(1,2)
  if binary_flip%2 == 0:
    result = "Heads"
  else:
    result = "Tails"
  print("The coin landed on " + result)
  if result == prediction:
    return True
  else:
    return False


def get_prediction():
    print("Do you predict 'Heads' or 'Tails'?")
    prediction = input("Press 'H' for 'Heads' and 'T' for 'Tails': ").upper()
    while prediction != "H" or prediction != "T": 
        if prediction == "H":
            return "Heads"
        elif prediction == "T":
            return "Tails"
        else:
            print("You have not made a valid selection.")
            prediction = input("Press 'H' for 'Heads' or 'T' for 'Tails': ").upper()

def play_coin_flip():
    print("You are betting on a coin toss." )
    bet = get_bet(money)
    prediction = get_prediction()
    result = coin_flip(prediction)
    return update_cash(money, bet, result)

def chohan(prediction):
    d_one = random.randint(1,6)
    d_two = random.randint(1,6)
    summation = d_one + d_two
    print("The two dice tallied to " + str(summation))
    if summation % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    if result == prediction:
        return True
    else:
        return False
def get_chohan_prediction():
    print("Do you predict 'Odd' or 'Even'?")
    prediction = input("Press 'O' for 'Odd' or 'E' for 'Even': ").upper()
    while prediction != "O" or prediction != "E": 
        if prediction == "O":
            return "Odd"
        elif prediction == "E":
            return "Even"
        else:
            print("You have not made a valid selection.")
            prediction = input("Press 'O' for 'Odd' or 'E' for 'Even': ").upper()

def play_chohan():
    print("The game is called Cho-Han. To win a player must predict correctly if the sum of two dice rolls is even or odd.")
    bet = get_bet(money)
    prediction = get_chohan_prediction()
    result = chohan(prediction)
    return update_cash(money, bet, result)



def play_cards():
    print("""
For this game you are player one and your opponent is player two.
The cards will be drawn at random and the highest card value wins.
Number cards have their face value.
Aces have a value of 1.
Jacks have a value of 11.
Queens have a value of 12.
Kings have a value of 13.
""")
    bet = get_bet(money)
    cards = [i for i in range(1, 14)]
    for i in range(1, 4):
        for j in range(1, 14):
            cards.append(j)
    cards.sort()
    number_of_cards = len(cards)
    first_players_card = cards.pop(random.randint(1, number_of_cards-1))
    number_of_cards -=1
    second_players_card = cards.pop(random.randint(1, number_of_cards-1))
    print("First player selected a " + str(first_players_card))
    print("Second player selected a " + str(second_players_card))
    if first_players_card > second_players_card:
        return update_cash(money, bet, True)
    elif first_players_card < second_players_card:
        return update_cash(money, bet, False)
    else:
        print("You draw")
        print("You have $" + str(money))

def roulette():
    print("This game is a simplified roulette table.")
    bet = get_bet(money)
    prediction = get_roulette_prediction()
    table = [i for i in range(0, 38)] #number 37 is '00' 
    ball = random.randint(0, 38)
    result = table[ball]
    if result != 37:
        print("The ball landed on " + str(result))
    else:
        print("The ball landed on 00")

    if result % 2 == 0 and prediction == "Even":
        return update_cash_roulette(money, bet, prediction)
    elif result % 2 == 1 and prediction == "Odd" and result != 37:
        return update_cash_roulette(money, bet, prediction)
    elif result  == 0 and prediction == "Zero":
        return update_cash_roulette(money, bet, prediction)
    elif result == 37 and prediction == "Double Zero":
        return update_cash_roulette(money, bet, prediction)
    else:
        return update_cash_roulette(money, bet, "Loss")
  
            
def get_roulette_prediction():
    print("""
For our basic roulette select from the following:
The ball will land on
Press   'O' for 'Odd' with a payout of 2 to 1,
        'E' for 'Even' with a payout of 2 to 1,
        'Z' for '0' with a payout of 35 to 1,
        'D' for '00' with a payout of 35 to 1.
        """)
    prediction = input("Make a selection: ").upper()
    while prediction != "O" or prediction != "E" or prediction != 'Z' or prediction != 'D': 
        if prediction == "O":
            print("You have predicted Odd")
            return "Odd"
        elif prediction == "E":
            print("You have predicted Even")
            return "Even"
        elif prediction == "Z":
            print("You have predicted Zero")
            return "Zero"
        elif prediction == "D":
            print("You have predicted Double Zero")
            return "Double Zero"
        else:
            print("You have not made a valid selection.")
            prediction = input("Make a selection: ").upper()
def update_cash_roulette(money, bet, result):
    if result == "Even" or result == "Odd":
        winnings = (money-bet) + bet*2
        print("You won. You now have $" + str(winnings)) 
        return winnings
    elif result == "Zero" or result == "Double Zero":
        winnings = (money-bet) + bet*35
        print("You won. You now have $" + str(winnings))
        return winnings
    else:
        loss = money - bet
        print("You lost. You now have $" + str(loss))
        return loss
    
#Call your game of chance functions here
while money > 0:
    money = play_coin_flip()
    if money == 0:
        print("You're out of cash!")
        break
    money = play_chohan()
    if money == 0:
        print("You're out of cash!")
        break
    money = play_cards()
    if money == 0:
        print("You're out of cash!")
        break
    money = roulette()
    again = input("To play again press any key. To quit just press return. ")
    if again == "":
        print("You finished gambling with $" + str(money) + ". Good Job")
        break
    
