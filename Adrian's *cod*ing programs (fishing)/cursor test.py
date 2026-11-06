'''
import curses
def main(stdscr):
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    curses.mouseinterval(0)

    stdscr.addstr(0, 0, "Move your mouse around the terminal. Press Q to quit.")

    while True:
        event = stdscr.getch()

        if event == curses.KEY_MOUSE:
            try:
                _, x, y, _, state = curses.getmouse()
                stdscr.addstr(2, 0, f"Mouse position: x={x}, y={y}   ")
                stdscr.refresh()
            except curses.error:
                pass

        elif event in (ord('q'), ord('Q')):
            break

curses.wrapper(main)
'''
import os
import sys
import tty
import termios
import select
import re

def track_mouse():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    pattern = re.compile(rb'\x1b\[<(\d+);(\d+);(\d+)([Mm])')
    buffer = bytearray()

    try:
        tty.setcbreak(fd)

        sys.stdout.write("\033[?1003h\033[?1006h")
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

        last_pos = None

        while True:
            ready, _, _ = select.select([fd], [], [], None)

            if ready:
                buffer.extend(os.read(fd, 4096))

            while True:
                match = pattern.search(buffer)

                if not match:
                    if len(buffer) > 32:
                        del buffer[:-32]
                    break

                _, x, y, action = match.groups()
                del buffer[:match.end()]

                pos = (int(x), int(y))

                if pos != last_pos:
                    last_pos = pos

                    sys.stdout.write(
                        f"\033[1;1HMouse X: {pos[0]}  Y: {pos[1]}     "
                    )
                    sys.stdout.flush()

    except KeyboardInterrupt:
        pass

    finally:
        sys.stdout.write("\033[?1003l\033[?1006l\033[0m")
        sys.stdout.flush()
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

track_mouse()
