import random 
import math

def get_value(card):
    value = math.ceil(card/4)
    if value == 1:
        return 11
    elif value > 10:
        return 10
    else:
        return value
    
def get_color(card):
    if card % 4 == 1:
        return "♥︎"  
    elif card % 4 == 2:
        return "♠︎" 
    elif card % 4 == 3:
        return "♦︎" 
    else:
        return "♣︎"

def DP_Ace_Ace():
    if deal_2_Player  == 22:
        return 12
    else:
        return deal_2_Player 

def DD_Ace_Ace():
    if deal_2_Dealer == 22:
        return 12
    else:
        return deal_2_Dealer 

Bank = 1000 #kr       
print(f"Player has {Bank} dollers in his bank")       
Bet = 50 #int(input("How much do you want to bet"))



cards = [x for x in range(1,53)]

random.shuffle(cards)

deal_1_Player =  get_value(cards.pop()) 
deal_1_Dealer =  get_value(cards.pop())

if deal_1_Dealer == 11 or 10:
    print("Dealer can have Blackjack")
else:
    print("m")

deal_2_Player = deal_1_Player + get_value(cards.pop())
deal_2_Dealer = deal_1_Dealer + get_value(cards.pop())


#if deal_2_Dealer == 21:
#avsluta splet och dealer vann 


if deal_2_Player == 21:
    print("Blackjack")#avsluta splet dubbla bet
    Bet = Bet*2
    Bank = Bank + Bet
else:
    print(f"{deal_2_Player} Player's Hand") 

print(f"{deal_1_Dealer} Dealer's Hand")

while True:
    if deal_2_Player > 21:
        break
    if deal_2_Player == 21:
        break
    Player_input = input("Stand or hit? (s/h): ") 
    if Player_input.lower() == "h":
        deal_2_Player =+ deal_2_Player + get_value(cards.pop())
        print(deal_2_Player)
    else: 
        break

if deal_2_Player > 21:
    print("Bust")
    Bank = Bank - Bet
elif deal_2_Player == 21:
    print("Blackjack")
    Bet = Bet * 2
    Bank = Bank + Bet
else:
    print(deal_2_Player)
    print(deal_2_Dealer)

while True:

    if deal_2_Dealer < 17:
        print("Dealer hits")
        deal_2_Dealer =+ deal_2_Dealer + get_value(cards.pop())
        print(deal_2_Dealer)
    elif 21 == deal_2_Dealer >= 17: 
        print("Dealer stands")
        break
    elif deal_2_Dealer > 21:
        print("Dealer is bust")
        break
    else:
        break


#skapa en granskning om betet 
if 21 >= deal_2_Player > deal_2_Dealer:
    print("Player win")
    Bet = Bet * 2
    Bank = Bank + Bet   
elif deal_2_Dealer > 21 and deal_2_Player <= 21:
    print("Player win")
    Bet = Bet * 2
    Bank = Bank + Bet
elif 21 >= deal_2_Dealer > deal_2_Player:
    print("DEALER WIN")
    Bank = Bank - Bet
elif deal_2_Player > 21 and deal_2_Dealer <= 21:
    print("DEALER WIN")
    Bank = Bank - Bet
elif deal_2_Dealer == deal_2_Player:
    print("player is pushed") 
    Bank = Bank + Bet
else:
    print("how") #how



print(Bank)