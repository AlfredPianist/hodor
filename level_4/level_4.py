#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hodor voting contest: level 4

Script that votes exactly 'votes_total' times for a given ID.

Using the 'requests' module, this task requires to send as POST the ID, the
'holdthedoor' fields for which to properly tally a vote, and a key field from
the form hidden from view.

It generates a valid User-Agent from the user_agent module and pushes it into
the HTTP request headers to validate the vote. Only Windows users are
able to vote.

It also includes the referred URL to the HTTP requests header as a way to
validate the vote.

It needs a proxy list to bypass the restriction of one vote per day per person.
Please provide a proxy list as a file named http_proxies.txt, this module will
cycle through all proxies provided until the target votes are met.

It also uses the 're' module searching the number of votes from a given ID,
and 'islice' from 'itertools' for the regex to find only 2 numeric instances
(ID and number of votes).
"""

import requests
import user_agent
import re
from itertools import islice, cycle

votes_total = 98

url = "http://158.69.76.135/level4.php"
user_ag = user_agent.generate_user_agent()
headers = {'user-agent': user_ag, 'referer': url}
session = requests.Session()
session.headers.update(headers)
success_txt = "Hold the Door challenge - Level 4"

try:
    proxies = open('http_proxies.txt', 'r')
except IOError:
    print("Proxy list non existent. Please provide one.")
    exit(1)
finally:
    proxy_set = set()
    for proxy in proxies:
        proxy_set.add(proxy[:-1])
    proxies.close()
    proxy_pool = cycle(proxy_set)

search_votes = session.get(url, headers=headers)
if search_votes.status_code != 200:
    print("Couldn't connect to the website. Try again later.")
    exit(1)
content = search_votes.text

print("Welcome to the Hodor voting contest!!")

is_number = False
while not is_number:
    print("Please insert your ID for placing your {:d} votes, \
or 'e' to exit.".format(votes_total))
    vote_id = input('ID: ')
    if vote_id == "e":
        exit(0)
    try:
        vote_id = int(vote_id)
        if vote_id < 0:
            print("Please insert a valid ID, or 'e' to exit.")
        else:
            payload = {'id': vote_id, 'holdthedoor': 'Submit'}
            is_number = True
    except TypeError:
        print("Please insert a valid ID.")

try:
    vote_row = "<tr>\n    <td>\n{:d}    </td>".format(vote_id)
    index_vote = content.index(vote_row)
    slice_int_row = islice(re.finditer(r'\d+', content[index_vote:]), 2)
    vote_id, votes = map(int, (num.group() for num in slice_int_row))
except ValueError:
    print("ID non existent. Creating new ID...")
    votes = 0

print("{:d} initial votes for ID {:d}.".format(votes, vote_id))

if votes >= votes_total:
    print("Can't vote more than {:d} times in this contest. \
Select another ID.".format(votes_total))
    exit(1)

votes_ok, votes_fail = 0, 0
while (votes + votes_ok < votes_total):
    try:
        search_key = session.get(url, headers=headers)
        content = search_key.text
        index_key = content.index("value=") + 7
        payload['key'] = content[index_key:index_key + 40]
    except ValueError:
        print("Couldn't fetch key.")
        votes_fail += 1
    try:
        proxy = next(proxy_pool)
        post = session.post(url,
                            data=payload,
                            proxies={"http": "http://" + proxy},
                            timeout=12)
        if post.status_code == 200 and success_txt in post.text:
            votes_ok += 1
            print("+1 vote. Total votes = {:d}.".format(votes + votes_ok))
        else:
            print("Couldn't vote. Trying again...")
            votes_fail += 1
    except Exception as exc:
        print(exc)
        votes_fail += 1

print("""Finished voting!
{:d} votes added with a total of {:d}.
Total votes failed: {:d}
Thanks for playing!!""".format(votes_ok, votes + votes_ok, votes_fail))
