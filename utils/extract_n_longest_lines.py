# requires python 3.6 or later (fstrings)

from heapq import heappush, heappop, heappushpop
import sys

MAX_HEAP_ENTRIES = 2000
OUTPUT_FILE = 'heaped.out.txt'
STATUS_EVERY = 1000

if len(sys.argv) != 2:
    raise SystemExit("Error: Must supply input filename as single argument.")


current_heap_length = 0
lineheap = list()
lines_processed = 0

with open(sys.argv[1], 'r') as f:
    print("Working...", end='')
    while True:
        line = f.readline()
        if not line:
            break
        line = line.rstrip()

        if current_heap_length >= MAX_HEAP_ENTRIES:
            garbage = heappushpop(lineheap, [len(line), line])
        else:
            heappush(lineheap, [len(line), line])
            current_heap_length+=1
        lines_processed+=1
        if lines_processed % STATUS_EVERY == 0:
            print(".", end='')
print()
print(f"Finished processing {lines_processed} lines.")


with open(OUTPUT_FILE, 'w') as of:
    for i in range(len(lineheap)):
        popped = heappop(lineheap)
        lineout = f"{str(popped[0])} | {popped[1]} \n"
        of.writelines(lineout)

