# hodor - [Level 4](http://158.69.76.135/level4.php)

- **Objective:** vote 98 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents*, the `itertools` module for cycling through the proxy list, and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- For obtaining a sizeable amount of votes, a proxy list must be used to bypass the day-between-votes restriction.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".
