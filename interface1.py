import curses
from curseXcel import Table


def main(stdscr):
    x = 0
    table = Table(stdscr, 10, 2, 5, 20, 30, spacing=1, col_names=True)
    m = 0
    while m < 2:
        table.set_column_header("Col " + str(m+1), m)
        m += 1
    m = 0
    while m < 10:
        n = 0
        while n < 2:
            table.set_cell(m, n, n+m)
            n += 1
        m += 1
#    table.delete_row(2)
    while (x != 'q'):
        table.refresh()
        x = stdscr.getkey()
        if (x == 'KEY_LEFT'):
            table.cursor_left()
        elif (x == 'KEY_RIGHT'):
            table.cursor_right()
        elif (x == 'KEY_DOWN'):
            table.cursor_down()
        elif (x == 'KEY_UP'):
            table.cursor_up()


def start_screen(stdscr):
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)


def stop_screen(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()


if __name__ == '__main__':
    stdscr = curses.initscr()
    start_screen(stdscr)

    curses.wrapper(main)

    stop_screen(stdscr)
