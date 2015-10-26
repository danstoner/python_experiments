import os

aline = '''
*****************************************
'''

#
# ascii art cat retrieved from http://user.xmission.com/~emailbox/ascii_cats.htm
# and slightly modified to work inside a Python script.
#
acat = '''
                                 
      ,/|         _.--''^``-...___.._./;
     /, \ '.     -'          ,--,,,--''
    ( \    `_-''       '    /)
     `;;'            ;   ; ;
       ._.--''     ._,,, _..' -.;.'
        (,_....----''      (,..--''

************* CAT DETECTED! *************
'''

def alert ():
    alarming = True
    x = None
    while alarming:
        print acat
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

    


print aline
print "CAT DEFENSE SYSTEM INITIALIZED"
print aline

try:
    while True:
        print "Press CTRL-C to abort (stop the program)"
        print ""
        input_code = raw_input ("Ready to scan: ")
        if input_code == "abcdefg":
            alert();
except (KeyboardInterrupt, EOFError) as e:
    print ""
    print aline
    print "Stopping!"
    print ""

