# initial start from http://www.dev-explorer.com/articles/python-with-curses

import curses
import curses.textpad

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

prompt_left_pos = 0
prompt_top_pos = 2

screen.addstr("CAT DEFENSE SYSTEM\n\n\n")
screen.addstr(prompt_top_pos, prompt_left_pos, "Ready to Scan: ")

textbox = curses.textpad.Textbox(screen)

acat = "meow\n\n"
aline = "******************************\n\n"

cat_codes = ('123456', 'abcdefg')

def alert ():
    alarming = True
    x = None
    while alarming:
        print acta
        print aline
        # bash command does two things:
        #   1. first play an alert sound
        #   2. use the operating system (shell) "read" command, 
        #      store the return code in variable x. 
        #      A return code of 0 means input was detected.
        x = os.system("""bash -c 'aplay -q sounds/alert.wav; read -s -t 1 -n 1 -p "Press ENTER to stop the alarm..."'""")

        print ""
        if x == 0: 
            alarming = False
            print "Alarm Stopped."
            print aline
        print aline


try:        
    while True:
        scanned = textbox.edit()
        #scanned = textbox.gather()
        screen.addstr(10,0,"CAT DEFENSE SYSTEM\n\n\n")
        #screen.addstr("******scanned*******")
        if scanned in cat_codes:
            alert()
        else:
            screen.addstr(10,0,"Nope\n\n")
        #event = screen.getch()
        #if event == ord("q"): break
        screen.refresh()
except KeyboardInterrupt:
    pass

curses.endwin()





