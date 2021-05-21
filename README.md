# Google Form Filler (GFF) - Automate your google form here!

## About

The idea of this project came from my online lectures as one of my professors takes attendance on a google form and what he does is, he sets the form "ON" for responses for any 5 min between the lecture but what if I'm sleeping, not attentive,
scrolling through my Instagram feed, or maybe eating something and I dont want to touch my laptop?

So I got to know about the module named selenium and I decided to make a script/code which will mark my attendance on google form even if I am not in front of the system.

## Working

This is how the script works:

1. When you run the code it launches the browser and opens provided google form link.
2. After that it checks whether the form is accepting responses or not,If form is closed
  for responses it refreshes the page after a specified interval.
3. And When code gets the response that the google form is accepting the responses it automatically
  fills my data in the google form and submit it on my behalf.

Now I can go to sleep, eat or scroll peacefully! ;)

## Dependencies

This project uses following dependencies in Python (install using `pip`):

* `selenium`
* `WebDriver`

Compatible with: Any PC or laptop with Python and Selenium installed on Chrome, Safari, Opera and Edge. _(Just modify the code accordingly)_

## Installation

1. Install `Python` (Any 3.x.x version)
2. Install `selenium` (https://pypi.org/project/selenium/)
3. Install `Webdriver` (For Chrome: https://chromedriver.chromium.org/, similarly find specific driver for your browser)

## Usage

1. Make sure you have the dependencies installed and have followed the steps mentioned in _Installation_ section above.
2. Make sure you have entered correct information of your webdriver in the code.
3. Replace all the existing links and data according to your need.
4. Execute: `python Google_form_filler.py`