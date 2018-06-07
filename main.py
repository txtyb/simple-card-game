import time,random

cardrange = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

#print(newcard)
cards = list()

def roundstart():
    newcard = random.choice(cardrange)
    cards.append(newcard)
    print(cards)

def gamechecker():
    s_card_position=-1
    for s_card in cards:
        print('s_card is:%s'%s_card)
        s_card_position+=1
        print('s_position is:%s'%s_card_position)
        e_card_position=cards[s_card_position:].index(s_card)
        print(s_card_position,e_card_position)

for i in range(1,8):
    roundstart()
    gamechecker()
