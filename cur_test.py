import curses

s = curses.initscr()
hei, wei = s.getmaxyx()
curses.start_color()                    
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)                                   
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)                                     
w = curses.newwin(0,0)
for i in range(1, int(wei)-1):
    w.addstr(0, i, '-')
w.addstr(0, 0, '↱')
w.addstr(0, int(wei)-1, '↰')
w.addstr(0, int(wei/2), '@')

for i in range(1, int(wei)-1):
    w.addstr(10, i, '-')
   # w.addstr(10, 10, '@')
w.refresh()
