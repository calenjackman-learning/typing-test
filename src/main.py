#!/usr/bin/env python3

import curses
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Typing Speed Test!!!\n')
    stdscr.addstr('Press any key to begin!')
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, "WPM: {wpm_display}".format(wpm_display=wpm))

    for i, char in enumerate(current):
        character_correct = target[i] == current[i]
        color = curses.color_pair(1) if character_correct \
            else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def load_text(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text("../samples.txt")
    current_text = []
    wpm = 0
    start_time = time.time()

    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        # assuming that the average length of a word is 5 characters
        wpm = round(((len(current_text) / time_elapsed)*60)/5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            input_key = stdscr.getkey()
        except:
            continue

        if ord(input_key) == 27:
            break

        if input_key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(input_key)


def main(stdscr):
    stdscr = stdscr
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


if __name__ == '__main__':
    curses.wrapper(main)
