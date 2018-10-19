##from colors import red, green, blue
##print red('This is red')
##print green('This is green')
##print blue('This is blue')
##
##from colors import color
##for i in range(256):
##    print (color('Color #%d' % i, fg=i))

##class bcolors:
##    HEADER = '\033[95m'
##    OKBLUE = '\033[94m'
##    OKGREEN = '\033[92m'
##    WARNING = '\033[93m'
##    FAIL = '\033[91m'
##    ENDC = '\033[0m'
##
##    def disable(self):
##        self.HEADER = ''
##        self.OKBLUE = ''
##        self.OKGREEN = ''
##        self.WARNING = ''
##        self.FAIL = ''
##        self.ENDC = ''
##        
##print (bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" 
##      + bcolors.ENDC)


import curses

# initialize curses
stdscr = curses.initscr()
##curses.noecho()
##
##begin_x = 20; begin_y = 7
##height = 5; width = 40
##win = curses.newwin(height, width, begin_y, begin_x)
##
curses.start_color()
####
##### initialize color #1 to Blue with Cyan background
####curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
####
####stdscr.addstr('A sword and a shield.', curses.color_pair(1))
####stdscr.refresh()
##
####stdscr.addstr(0, 0, "Current mode: Typing mode",
####              curses.A_REVERSE)
####stdscr.addstr(0, 0, "Current mode: Typing mode",
####              curses.A_BLINK)
####stdscr.refresh()
##pad = curses.newpad(100, 100)
### These loops fill the pad with letters; addch() is
### explained in the next section
##for y in range(0, 99):
##    for x in range(0, 99):
##        pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
##
### Displays a section of the pad in the middle of the screen.
### (0,0) : coordinate of upper-left corner of pad area to display.
### (5,5) : coordinate of upper-left corner of window area to be filled
###         with pad content.
### (20, 75) : coordinate of lower-right corner of window area to be
###          : filled with pad content.
##pad.refresh( 0,0, 5,5, 20,75)
stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_BOLD)
stdscr.addstr(1, 1, "Current mode: Typing mode",
              curses.A_DIM)
stdscr.refresh()
##
### finalize curses
can_change_color()
##curses.nocbreak()
##stdscr.keypad(False)
##curses.echo()
curses.endwin()
input("Press enter to exit. ")


