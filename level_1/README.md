# hodor - [Level 1](http://158.69.76.135/level1.php)

- **Objective:** vote 4096 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents* and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".
