import os
import subprocess
import threading
import curses
curses.mousemask(curses.ALL_MOUSE_EVENTS)
curses.mouseinterval(0)
def movement():
    while True:
        event = stdscr.getch()

        if event == curses.KEY_MOUSE:
            try:
                _, x, y, _, state = curses.getmouse()
                print(f"Mouse position: x={x}, y={y}   ")
            except curses.error:
                pass



cursortrack = threading.Thread(target=movement, daemon=True)
cursortrack.start()
command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
subprocess.run(command)
print(f"Move your mouse around the terminal. Press Q to quit.")
elif event in (ord('q'), ord('Q')):
    break

