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

SEARCH_URL='http://search.idigbio.org/v2/search/'
QUERY_TYPE = 'mq'
INPUT_QUERY={ "genus": "Acer"}


r = requests.get(f"{SEARCH_URL}?{QUERY_TYPE}&fields=uuid", json=INPUT_QUERY)
media_urls = r.content

print(media_urls)

raise SystemExit

# create a re-usable session object
session = FuturesSession(max_workers=8) # 8 is default


futures = []

future = session.get(f"{SERVICE_URL}?{QUERY_TYPE}", json=INPUT_QUERY)
futures.append(future)

# for iterator ...
#         future = session.get(url, json=json_stuff))
#         future.url = url
#         futures.append(future)

logfile = open(OUTPUT_FILENAME, "w")
outfile = open(OUTPUT_FILENAME, "wb")

for future in as_completed(futures):
    r=future.result()
    logline = (f"{datetime.now()},{r.status_code},{r.url}\n")
    logfile.write(logline)
    # Also print the "log" to stdout
    print(logline, end="")

outfile.close()
logfile.close()
