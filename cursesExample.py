import sys,os
import curses

def draw_menu(stdscr):
    key = 0
    a = 0
    b = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Loop where k is the last character pressed
    while (key != ord('z')):

        # Initialization
        stdscr.clear()
  
        if key == ord('a'):
            a += 1
        elif key == ord('b'):
            b += 1
        
        #get terminal size
        height, width = stdscr.getmaxyx()

        # Declaration of strings
        title = "Curses example"[:width-1]
        line1 = "a {}".format(a)[:width-1]
        line2 = "b {}".format(b)[:width-1]
        line3 = "Click z to quit"[:width-1]

        # Get center dimmesions 
        start_x = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_y = int((height // 2) - 2)

        # Print text
        stdscr.addstr(start_y, start_x, title)

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(start_y + 1, start_x, line1)
        stdscr.attroff(curses.color_pair(1))

        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(start_y + 3, start_x, line2)
        stdscr.attroff(curses.color_pair(2))

        stdscr.addstr(start_y + 5, start_x, line3)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        key = stdscr.getch()


def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()