"""
This is a sample that can take download a lot of urls
quickly using Python Futures.

This is the multi-threaded version.
"""

import requests
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
import json
from datetime import datetime


OUTPUT_FILENAME = f"multi_fetcher.log"

SERVICE_URL='http://search.idigbio.org/v2/search/'
QUERY_TYPE = 'mq'
INPUT_QUERY={ "genus": "Acer"}


r = requests.get(f"{SERVICE_URL}?{QUERY_TYPE}&fields=uuid", json=INPUT_QUERY)
media_urls = r.content

print(media_urls)

raise SystemExit

# create a re-usable session object
session = FuturesSession(max_workers=8) # 8 is default


futures = []

future = session.get(f"{SERVICE_URL}?{QUERY_TYPE}", json=INPUT_QUERY)
futures.append(future)

# with open(INPUT_FILENAME, "r") as f:
#     for line in f:
#         # This is hard-coded to parse a specific "sequence of curl commands" line format
#         # and depends on the ONLY single-quoted string being the JSON delimiter.  Actually it should
#         # work on any input file where the JSON section is quoted with single quotes and there is no other
#         # similarly quoted value in the line.
#         #
#         # A sample line looks like the following (there is an added a line break for readability
#         # and the JSON is trimmed for space):
#         #
#         #   curl --silent --show-error -i -X POST -H "Content-Type: application/json"
#         #     -d '{"version": 1.0, <...>  }' http://wsbeta3.iris.washington.edu:8089/iriswsbeta/usage-stats/1/submit
#         #
#         # Output file will be comma-delimited:
#         #  timestamp, HTTP request status code, JSON body that was POSTed.
#         #
#         json_as_string = line.split("'")[1]
#         future = session.post(SERVICE_URL, json=json.loads(json_as_string))
#         future.json_as_string = json_as_string
#         futures.append(future)

logfile = open(OUTPUT_FILENAME, "w")
outfile = open(OUTPUT_FILENAME, "wb")

for future in as_completed(futures):
    r=future.result()
    outfile.write(r.content)
    logline = (f"{datetime.now()},{r.status_code}\n")
    logfile.write(logline)
    # Also print the "log" to stdout
    print(logline, end="")

outfile.close()
logfile.close()
