import os

line = '''
*****************************************
'''

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
        print line
        # bash command does two things:
        #   first play an alert sound (/usr/share/sounds/purple/alert.wav from Ubuntu)
        #   x receives the return code from the operating system "read" command, success = 0
        x = os.system("""bash -c 'aplay -q alert.wav; read -s -t 1 -n 1 -p "Press ENTER to stop the alarm..."'""")

        print ""
        if x == 0: 
            alarming = False
            print "Alarm Stopped."
            print line
        print line

    


print line
print "CAT DEFENSE SYSTEM INITIALIZED"
print line

try:
    while True:
        print "Press CTRL-C to abort (stop the program)"
        print ""
        input_code = raw_input ("Ready to scan: ")
        if input_code == "abcdefg":
            alert();
except (KeyboardInterrupt, EOFError) as e:
    print ""
    print line
    print "Stopping!"
    print ""

