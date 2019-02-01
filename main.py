import time, random, curses

score=0
cardrange = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

##print(newcard)
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
    for i in range(len(dcards)-1,-1,-1):
        cards.append(dcards[i])
        #将卡片倒序排列
    #print('回合开始时的卡片：',cards)

def gamechecker():
    '''是否得分判断'''
    s_card_pos=0
    global e_card_pos
    s_card=cards[s_card_pos]
    #for s_card in cards:
        ##print('s_card is:%s'%s_card)
        #s_card_pos+=1
        ##print('s_pos is:%s'%s_card_pos)
    try:
        e_card_pos = cards[s_card_pos+1:].index(s_card)
    except ValueError:
        #print('没有得分点')
        pass
    else:
        #print('发现得分点')
        e_card_pos+=1
        #重要！切分s_card_pos时产生了新的列表，这使得e_card_pos少了1
        #print('e_card_pos=%s'%e_card_pos)
        cards_num=e_card_pos-0
        scount(cards_num)
        rm()
        return

def rm():
    rmcards=cards[:e_card_pos+1]
    #print('rmcards= ',rmcards)
    for percard in rmcards:
        cards.remove(percard)
        #清除得分的卡片
    #print('清除后：',cards)

def scount(num):
    '''得分计算部分，尚未完成'''
    global score
    score+=num*5

def initdesk():
    s = curses.initscr()
    global hei, wei
    hei, wei = s.getmaxyx()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()                    
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)                                   
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)                                     
    global w
    w = curses.newwin(0,0)
    # 画出desk
    for i in range(1, int(wei)-1):
        w.addstr(0, i, '-')
        w.addstr(int(hei)-1, i, '-')
    w.addstr(0, 0, '↱')
    w.addstr(0, int(wei)-1, '↴')
    w.addstr(int(hei)-1, int(wei)-2, '↵')
    w.addstr(int(hei)-1, 0, '↳')
    for i in range(1, int(hei)-1):
        w.addstr(i, 0, '|')
        w.addstr(i, int(wei)-1, '|')
    w.refresh()
# def main():
    
initdesk()
while True:
    # 清除前一次绘制的card
    for i in range(1, int(wei)-1):
        w.addstr(int(hei/2), i, ' ')
    roundstart()
    gamechecker()
    # 绘制score
    w.addstr(3, 2, 'Score:'+str(score))
    # 绘制card
    w.attron(curses.color_pair(2))
    w.addstr(int(hei/2), int(wei/2), str(cards))
    w.attroff(curses.color_pair(2))
    #print('score=%s'%score)
    key = w.getch()
    # q键退出游戏
    if key == ord('q'):
        curses.endwin()
        quit()
    elif key != -1:
        pass
