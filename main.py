import time,random

score=0
cardrange = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

#print(newcard)
dcards = list()
cards = list()

def roundstart():
    '''回合开始发卡片'''
    dcards.clear()
    for i in range(len(cards)-1,-1,-1):
        dcards.append(cards[i])
        #初始化dcards，以从cards传回更改
    newcard = random.choice(cardrange)
    dcards.append(newcard)
    cards.clear()
    #清空卡片避免造成叠加重复
    #print('dcards= ',dcards)
    for i in range(len(dcards)-1,-1,-1):
        cards.append(dcards[i])
        #将卡片倒序排列
    print('回合开始时的卡片：',cards)

def gamechecker():
    '''是否得分判断'''
    s_card_position=0
    global e_card_position
    s_card=cards[s_card_position]
    #for s_card in cards:
        #print('s_card is:%s'%s_card)
        #s_card_position+=1
        #print('s_position is:%s'%s_card_position)
    try:
        e_card_position = cards[s_card_position+1:].index(s_card)
    except ValueError:
        print('没有得分点')
        #pass
    else:
        print('发现得分点')
        e_card_position+=1
        #重要！切分s_card_position时产生了新的列表，这使得e_card_position少了1
        print('e_card_position=%s'%e_card_position)
        # print(s_card_position,e_card_position)
        cards_num=e_card_position-0
        scount(cards_num)
        rm()
        return

def rm():
    rmcards=cards[:e_card_position+1]
    print('rmcards= ',rmcards)
    for percard in rmcards:
        cards.remove(percard)
        #清除得分的卡片
        print('清除后：',cards)

def scount(num):
    '''得分计算部分，尚未完成'''
    global score
    score+=num*5

while True:
    roundstart()
    gamechecker()
    print('score=%s'%score)
    input('---------------')
