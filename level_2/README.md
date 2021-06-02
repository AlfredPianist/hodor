# hodor - [Level 2](http://158.69.76.135/level2.php)

- **Objective:** vote 1024 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents* and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".
