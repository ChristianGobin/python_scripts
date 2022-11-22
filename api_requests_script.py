#!/usr/bin/env python3
#Use requests package to make a request to extract info from bloomberg api.

import requests

r = requests.get("https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete")

print(r.encoding)
print(r.content)