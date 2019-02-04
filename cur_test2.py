import curses
from time import sleep

def draw_main(w):
    w.addstr(1, 1, 'Test' )
    w.refresh()
    sleep(2)

def main():
    curses.wrapper(draw_main)

if __name__ == '__main__':
    main()
