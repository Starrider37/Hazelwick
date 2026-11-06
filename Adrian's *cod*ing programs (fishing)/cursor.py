
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
