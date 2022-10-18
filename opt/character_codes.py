import curses
import locale


def main(stdscr):

    while True:
        input_character = stdscr.getch()

        if input_character == 27:
            break

        stdscr.clear()
        stdscr.addstr(str(input_character))
        stdscr.refresh()


curses.wrapper(main)
