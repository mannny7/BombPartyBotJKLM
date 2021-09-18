from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

# Bomb party bot by Msesjrl
# Discord: Mannnny#0001
# Youtube video for install: https://www.youtube.com/watch?v=KxmgQc2nc4E&t=2s
# Paypal for donations: emerlee7@hotmail.com

mode = 0
extraInfo = 0

while mode == 0:
    try:
        mode = int(input(">>> Choose a mode by typing its number: \n 1. Blatant \n 2. Human like \n \n"))
    except:
        pass

if mode == 1:
    print("Blatant mode selected!")
else:
    print("Human like mode selected!")

while extraInfo == 0:
    try:
        extraInfo = int(input(">>> Choose if you would like additional "
                              "info printed by the bot: \n 1. Yes \n 2. No \n \n"))
    except:
        pass

if extraInfo == 1:
    print("Extra info will be provided!")
else:
    print("No extra info will be provided!")

selfPass = input("PRESS ENTER TO CONTINUE >>>")

for i in range(10):
    print("\n")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.jklm.fun")

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
path = CURR_DIR + "/web2"

wordlistone = open(path)
stringone = wordlistone.read()

while True:
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
        if mode == 2:
            if not driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
                arrayOfWords = []
                syllable = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div").text
                answerBox = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
                var = syllable

                for line in stringone.splitlines():
                    if var in line:
                        arrayOfWords.append(line)

                matchingWord = arrayOfWords[random.randint(0, len(arrayOfWords))]
                if extraInfo == 1:
                    print("Sent word", matchingWord)
                answerBox.click()
                time.sleep(random.randint(15, 65) / 100)
                for character in matchingWord:
                    characterCode = ord(character) + random.randint(1, 4)
                    fail = random.randint(1, 25)
                    if fail == 2: # Spelling mistakes algorithm
                        loops = random.randint(1, 3)

                        for i in range(loops):
                            answerBox.send_keys(chr(characterCode))
                            time.sleep(random.randint(2, 5) / 100)

                        time.sleep(0.1)

                        for i in range(loops):
                            answerBox.send_keys(Keys.BACK_SPACE)
                        time.sleep(0.1)
                        answerBox.send_keys(character)
                    elif fail == 15:
                        time.sleep(random.randint(25, 30) / 100)
                    else:
                        answerBox.send_keys(character)
                    time.sleep(random.randint(5, 14) / 100)
                answerBox.send_keys(Keys.RETURN)
                time.sleep(0.05)
        elif mode == 1:
            if not driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
                arrayOfWords = []
                syllable = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div").text
                answerBox = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
                var = syllable

                for line in stringone.splitlines():
                    if var in line:
                        arrayOfWords.append(line)

                matchingWord = arrayOfWords[random.randint(0, len(arrayOfWords))]
                if extraInfo == 1:
                    print("Sent word", matchingWord)
                answerBox.click()
                answerBox.send_keys(matchingWord)
                answerBox.send_keys(Keys.RETURN)
                time.sleep(0.01)
    except:
        pass
