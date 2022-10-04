#!/usr/bin/env python3

import curses
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Typing Speed Test!!!\n')
    stdscr.addstr('Press any key to begin!')
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = 'Hello world this is some test text for this application!'
    current_text = []

    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        input_char_code = stdscr.getch()

        if input_char_code == 27:
            break

        input_key = chr(input_char_code)

        if input_key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(input_key)



def main(stdscr):
    stdscr = stdscr
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

if __name__ == '__main__':
    curses.wrapper(main)
