# hodor - [Level 3](http://158.69.76.135/level3.php)

- **Objective:** vote 1024 for your Holberton School ID.
- Used the `requests` module for handling the HTTP request, the `user-agent` module for generation of valid *user-agents*, the `PIL` module for image processing and `pytesseract` OCR tool for image CAPTCHA recognition, and the `re` module for regular expression search.
- The browser's *user-agent* needs to exist in order to validate the vote. Only Windows systems are allowed.
- The *referer* HTTP request header is needed in order to validate the vote.
- The CAPTCHA must be solved as a requirement to validate the vote.
- Send as a POST request the ID, a "hidden" random key on the form, the captcha text and the Submit button called "holdthedoor".
