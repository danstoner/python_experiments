"""
Convert multi-line timestamped logfile to single lines to allow easy use of grep.

Requires each line in the input file to begin with a timestamp (actually,
a numeric digit) and other lines cannot begin with a digit.

Typically, log files that break over multiple lines also indent the additional lines.

For example, a postgesql server log.
"""
import sys


if len(sys.argv) < 2:
    print ("Error: must supply a filename for Input. Only the first arg will be processed")
    raise SystemExit

infile=sys.argv[1]

with open(infile, "r") as f:
    lastline = ""
    buffer = ""
    for line in f:
        if line[0].isdigit():
            if buffer == "":
                buffer += line.strip()
            else:
                print(buffer.replace("\t","")) # previous buffered line, stripping tabs
                buffer = line.strip()
        else:
            buffer += " " + line.strip()

    print(buffer.replace("\t","")) # final buffered line, stripping tabs
