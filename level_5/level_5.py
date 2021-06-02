#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Hodor voting contest: level 5

Script that votes exactly 'votes_total' times for a given ID.

Using the 'requests' module, this task requires to send as POST the ID, the
'holdthedoor' fields for which to properly tally a vote, and a key field from
the form hidden from view.

It generates a valid User-Agent from the user_agent module and pushes it into
the HTTP request headers to validate the vote. Only Windows users are
able to vote.

It also includes the referred URL to the HTTP requests header as a way to
validate the vote.

For deciphering the captcha, it uses the pytesseract and the PIL modules.
This image needed some preprocessing to help pytesseract decipher the captcha.

It also uses the 're' module searching the number of votes from a given ID,
and 'islice' from 'itertools' for the regex to find only 2 numeric instances
(ID and number of votes).
"""

import requests
import user_agent
import re
import os
from itertools import islice
import pytesseract
from PIL import Image, ImageFilter

votes_total = 1024

url = "http://158.69.76.135/level5.php"
captcha_url = "http://158.69.76.135/tim.php"
user_ag = user_agent.generate_user_agent(os='win')
headers = {'user-agent': user_ag, 'referer': url}
session = requests.Session()
session.headers.update(headers)
success_txt = "Hold the Door challenge - Tim Britton's special"

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

    captcha_resp = session.get(captcha_url, headers=headers)
    with open('captcha.png', 'wb') as captcha:
        captcha.write(captcha_resp.content)
    captcha = Image.open('captcha.png')
    captcha_data = captcha.load()
    height, width = captcha.size
    for h in range(height):
        for w in range(width):
            (r, g, b) = captcha_data[h, w]
            if (r, g, b) == (0, 0, 0) or (r, g, b) == (128, 128, 128):
                captcha_data[h, w] = 255, 255, 255
    captcha.filter(ImageFilter.BLUR)
    captcha.save('captcha.png', 'png')
    captcha_txt = pytesseract.image_to_string(Image.open('captcha.png'))
    payload['captcha'] = captcha_txt[:8]

    try:
        post = session.post(url, data=payload)
        if post.status_code == 200 and success_txt in post.text:
            votes_ok += 1
            print("+1 vote. Total votes = {:d}.".format(votes + votes_ok))
        else:
            # print("Couldn't vote. Trying again...")
            votes_fail += 1
    except Exception as exc:
        print(exc)
        votes_fail += 1

os.remove('captcha.png')
print("""Finished voting!
{:d} votes added with a total of {:d}.
Total votes failed: {:d}
Thanks for playing!!""".format(votes_ok, votes + votes_ok, votes_fail))
