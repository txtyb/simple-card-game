import time,random

score=0
cardrange = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

#print(newcard)
cards = list()

def roundstart():
    newcard = random.choice(cardrange)
    cards.append(newcard)
    print('回合开始时的卡片：',cards)

def gamechecker():
    for s_card in cards:
    # print('s_card is:%s'%s_card)
    # s_card_position+=1
    # print('s_position is:%s'%s_card_position)
        e_card_position = cards.index(s_card)
        print('e_card_position=%s'%e_card_position)
        # print(s_card_position,e_card_position)
        if e_card_position!=0:
            cards_num=e_card_position-0
            scount(cards_num)
            rmcards=cards[:e_card_position]
            for percard in rmcards:
                cards.remove(percard)
                #清除得分的卡片
                print('清除后：',cards)

def scount(num):
    global score
    score+=num*5

for i in range(1,8):
    roundstart()
    gamechecker()
    print('score=%s'%score)
