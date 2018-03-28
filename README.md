# Google Easter Eggs

This project is a functional testing example that tests for the functioning of several Google Search easter eggs.

## Requirements
* python 3
* `pip install selenium`
* Firefox or Chrome/Chromium
* latest geckodriver and chromedriver installed on `$PATH`
  * [geckodriver](https://github.com/mozilla/geckodriver/releases)
  * [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Running the test
To pick a browser, uncomment the line for the browser you want in config.py.
Or add another browser of your choosing (you will need to have the driver for that browser installed)

To start the test, run `python3 test.py`

## Notes & Considerations

* The test case itself took no more than 3-4 hours to write
* Issues with getting selenium to run correctly ate up time that could have been spent enhancing the test case
* There are some logical considerations for expanding the test suite:
  * Split the tests into seperate test case classes, and do unhappy path tests
  * Most of the tests only check for the most basic evidence of the easter egg working, so the next step would be to check that, for instance, zergs are actually spawning on the page.
  * I'm only checking for one invocation phrase, where some have multiple.
  * The `unittest` library doesn't seem to let you insert parameters on the command line, so easily switching between browsers, for instance, is difficult without editing a config file. I'd want to investigate the feature set of other libraries
  * There's a lot of code repetition that could have been moved out into helper functions, such as entering a search term
