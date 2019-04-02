import os
import sys

def make_big_random_file(filefullpath, size_in_mb):
    mb_written = 0
    with open(filefullpath,'wb') as outfile:
        while mb_written < size_in_mb:
            mb = os.urandom(1024 * 1024)
            outfile.write(mb)
            mb_written += 1                

if len(sys.argv)!= 2:
    print("Must supply one argument... desired size in MiB")
else:
    outfilename = '/tmp/' + str(sys.argv[1]) + 'MB_RANDOM_FILE'
    try:
        make_big_random_file(outfilename, int(sys.argv[1]))
        print("Created file: {0}".format(outfilename))
    except:
        print("Failed to create file: {0}".format(outfilename))
