### GatorLUG Codeslinger 2011 Problem
### http://www.gatorlug.org/node/315

### READ input from STDIN by running:
### python codeslinger.py < inputfile.txt

'''
Usage:
$ python codeslinger.py < tests/smallest.txt
apt pat tap
tap apt pat
care race

'''


from __future__ import print_function
import sys

def get_input (inputlines):
    for each in sys.stdin.readlines():
        inputlines.append(each.strip())
    return inputlines


def iter_each (w, myset):
    newset = myset.copy()

    if w in newset:
        newset.discard(w)

    answer = []
    answer.append(w)
    for item in sorted(newset):
        answer.append(item)
    print(*answer)


def main():
    input_content = get_input([])
    dictionary_length = int(input_content[0])

    results = {}

    x = 1
    while x <= dictionary_length:
        results[''.join(sorted(input_content[x]))] = {input_content[x]}

        x += 1

    words = input_content[x:]
    for each in words:
        #print (each)
        results[''.join(sorted(each))].add(each)
        #print (results)

    #print ("Results hash = {0}".format(results))
    
    for out_word in words:

        iter_each(out_word, results[''.join(sorted(out_word))])



if __name__ == "__main__":
    main()






