import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import config


class EasterEggsTestCase(unittest.TestCase):

    def setUp(self):
        if config.BROWSER == 'Firefox':
            self.browser = webdriver.Firefox()
        elif config.BROWSER == 'Chrome':
            self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get('https://google.co.uk/')
        self.browser.implicitly_wait(30)
        self.search_box = self.browser.find_element_by_id('lst-ib')

    def tearDown(self):
        self.browser.quit()

    def test_zerg_rush(self):
        self.search_box.send_keys('zerg rush')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('zergrush'))
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))

    def test_game_of_life(self):
        self.search_box.send_keys('conway\'s game of life')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('game-of-life'))
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))

    def test_fun_facts(self):
        self.search_box.send_keys('fun facts')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))
        # This easter egg is slightly different, but we can check for the
        # "Ask another question" button.
        self.assertIn(self.browser
                      .find_element_by_css_selector('p.fVJEf')
                      .get_attribute('innerHTML'),
                      'Ask another question')

    def test_festivus(self):
        self.search_box.send_keys('festivus')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))
        self.assertIn('background:url(\'/logos/2012/festivus_body.png\')',
                      self.browser
                      .find_element_by_css_selector('#easter-egg style')
                      .get_attribute('innerHTML'))
        self.assertIn('background:url(\'/logos/2012/festivus_top.png\')',
                      self.browser
                      .find_element_by_css_selector('#easter-egg style')
                      .get_attribute('innerHTML'))

    def test_anagram(self):
        self.search_box.send_keys('anagram')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))
        self.assertIn('nag a ram',
                      self.browser
                      .find_element_by_css_selector('.ssp a.spell i')
                      .get_attribute('innerHTML'))

    def test_barrel_roll(self):
        self.search_box.send_keys('do a barrel roll')
        self.search_box.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)
        self.assertTrue(self.browser.find_element_by_id('easter-egg'))
        self.assertIn('transform:rotate(360deg)',
                      self.browser
                      .find_element_by_css_selector('#easter-egg style')
                      .get_attribute('innerHTML'))

if __name__ == "__main__":
    unittest.main(verbosity=2)
