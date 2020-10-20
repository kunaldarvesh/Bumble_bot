#!/usr/bin/python3

from selenium import webdriver
from time import sleep
from random import random
from login import username, password

class bumble_bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://bumble.com/app')

        sleep(5)

        fb_log = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span')
        fb_log.click()

        basewindow = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        email_log = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_log.send_keys(username)
        pass_log = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_log.send_keys(password)
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(2)
        self.driver.switch_to_window(basewindow)
        sleep(7)

    def like(self):
        swipe_right = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        swipe_right.click()

    def dislike(self):
        swipe_left = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
        swipe_left.click()

    def auto_swipe(self):
        swipes = 1000
        like, dislike = 0,0
        while swipes > 0:
            sleep(2)
            try:
                rand = random()
                if rand < 1:
                    self.like()
                    swipes = swipes - 1
                    like += 1
                    print('{} likes'.format(like))
                else:
                    self.dislike()
                    dislike += 1
                    swipes = swipes - 1
                    print('{} dislikes'.format(dislike))
            except Exception:
                try:
                    self.boom()
                except Exception:
                    try:
                        pop_2 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/aside')
                        pop_2.click()
                    except Exception:
                        try:
                            pop_3 = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
                            pop_3.click()
                        except Exception:
                            break


    def boom(self):
        boom = bot.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div/span/span/span/span')
        boom.click()


bot = bumble_bot()
bot.login()
bot.auto_swipe()
