import random
p4='';p2='';p3=''
playerlist=list()
players=list()

#init
def init():
    global playerlist ,players
    playerlist=['JX','cjun','SB','luguode']
    for i in range(0,3):
        e=random.choice(playerlist)
        playerlist.remove(e)
        players.append(e)
    global p4 ,p2 ,p3
    p2, p3 ,p4=players[0], players[1] ,players[2]
    print('函数内：',p2,p3,p4)
    #print(players)

desk = '''
↱------------------------------------------↴
|                   %s  ♂                  |
|                                          |
|                                          |
|                                          |
| %s                %s                %s   |
|  ♂                                     ♂ |
|                                          |
|                                          |
|                                          |
|                                          |
|               🤔  WHH  ♂                 |
↳------------------------------------------↵
'''%(p3, p4, players, p2)

#debug
if __name__ == '__main__':
   while True:
        init()
        print('函数外：',p2,p3,p4)
        print(desk)
        players.clear()
        input('-----------------------------')
