import os

line = "*********************************"
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
        # x gets the return code from the operating system command, success = 0
        x = os.system("""bash -c 'read -s -t 1 -n 1 -p "Press ENTER to stop the alarm..."'""")

        print ""
        if x == 0: 
            alarming = False
            print "Alarm Stopped."
            print line
        print line

    


print line
print "CAT DEFENSE SYSTEM INITIALIZED"
print line

while True:
    input_code = raw_input ("Ready to scan: ")
    if input_code == "abcdefg":
        alert();
