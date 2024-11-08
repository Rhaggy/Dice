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
    

cards = [x for x in range(1,53)]

random.shuffle(cards)

sum_player =  get_value(cards.pop()) + get_value(cards.pop())
sum_dealer =  get_value(cards.pop())

print(f"Spelarens summa: {sum_player}")
print(f"Dealens summa: {sum_dealer}")
pi = input("H eller S").lower
while pi == "H":
    sum_player2 = sum_player + get_value(cards.pop())
    continue
    print(f"{sum_player2}")