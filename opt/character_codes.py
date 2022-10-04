import curses
import locale

def main(stdscr):

    while True:
        input_character = stdscr.getch()
        stdscr.clear()
        stdscr.addstr(str(input_character))
        stdscr.refresh()

locale.setlocale()
code = locale.getpreferredencoding()

curses.wrapper(main)
