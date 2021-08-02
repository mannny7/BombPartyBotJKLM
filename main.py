from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import keyboard
import string

# Party Bomb Bot by Msesjrl (Mannnny)
# Discord: Mannnny#5377
# Read the readme on GitHub it will fix most issues
# Please change line 17

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.jklm.fun")

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
path = CURR_DIR + "\web2"

wordlistone = open(path)
stringone = wordlistone.read()

while not keyboard.is_pressed('z'): # Press 'z' to stop program
    while True:
        try:
            driver.switch_to.frame(
                driver.find_element_by_xpath(
                    "//div[@class='game']/iframe[contains(@src,'jklm.fun')]")) # Switch to correct iframe
        except:
            break

    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/button").click() # Auto joins games
        except:
            break

    try:
        if not driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
            arrayOfWords = []
            syllable = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div").text
            answerBox = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
            var = syllable

            for line in stringone.splitlines():
                if var in line:
                    arrayOfWords.append(line)

            matchingWord = arrayOfWords[random.randint(0, len(arrayOfWords))]
            answerBox.click()

            for character in matchingWord:
                fail = random.randint(1, 12)
                if fail == 2: # Spelling mistakes algorithm
                    loops = random.randint(1, 3)

                    for i in range(loops):
                        answerBox.send_keys(random.choice(string.ascii_uppercase))
                        time.sleep(random.randint(3, 8) / 100)

                    time.sleep(0.1)

                    for i in range(loops):
                        answerBox.send_keys(Keys.BACK_SPACE)

                    time.sleep(0.1)
                    answerBox.send_keys(character)
                else:
                    answerBox.send_keys(character)
                time.sleep(random.randint(5, 14) / 100)
            answerBox.send_keys(Keys.RETURN)
            time.sleep(0.05)
    except:
        pass
