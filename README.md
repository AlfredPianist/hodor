# hodor - Online vulnerable voting contest

This is the 'hodor' repository for a Holberton online voting contest practicing some web hacking skills. For this challenge I used the Python programming language. Here's a description of each level:

## [Level 0](http://158.69.76.135/level0.php)

- **Objective:** vote 1024 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request and the `re` module for regular expression search.
- Send as a POST request the ID with the Submit button called "holdthedoor".

## [Level 1](http://158.69.76.135/level1.php)

- **Objective:** vote 4096 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents* and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".

## [Level 2](http://158.69.76.135/level2.php)

- **Objective:** vote 1024 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents* and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".

## [Level 3](http://158.69.76.135/level3.php)

- **Objective:** vote 1024 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents*, the `PIL` module for image processing and `pytesseract` OCR tool for image CAPTCHA recognition, and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- The CAPTCHA must be solved as a requirement to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form, the captcha text and the Submit button called "holdthedoor".

## [Level 4](http://158.69.76.135/level4.php)

- **Objective:** vote 98 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents*, the `itertools` module for cycling through the proxy list, and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- For obtaining a sizeable amount of votes, a proxy list must be used to bypass the day-between-votes restriction.
- Send as a POST request the ID, a "hidden" random key on the form and the Submit button called "holdthedoor".

## [Level 5](http://158.69.76.135/level5.php)

- **Objective:** vote 1024 for your Holberton School ID.

- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents*, the `PIL` module for image processing and `pytesseract` OCR tool for image CAPTCHA recognition, and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- The CAPTCHA must be solved as a requirement to validate the vote. This time, the image had to be preprocessed before feeding it to the OCR tool to better the chances of a correct recognition.
- Send as a POST request the ID, a "hidden" random key on the form, the captcha text and the Submit button called "holdthedoor".
