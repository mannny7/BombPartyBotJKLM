import json
import os
import random
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome import service as cs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def runBot():
    with open("settings.json", "r") as file:
        data = json.load(file)

    chance = data["chance"]
    pauseBetween = data["pause"]
    pauseBegin = data["begin"]
    mode = data["mode"]
    extraInfo = data["info"]

    fileLocation = os.path.dirname(os.path.realpath(__file__))
    filePath = fileLocation + "/chromedriver.exe"
    chrome_service = cs.Service(
        executable_path=filePath)
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://www.jklm.fun")

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    path = CURR_DIR + "/web2"

    wordlistone = open(path)
    stringone = wordlistone.read()

    while True:
        while True:
            try:
                driver.switch_to.frame(
                    driver.find_element(By.XPATH,
                                        "//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))  # Switch to correct iframe
            except:
                break

        while True:
            try:
                joinButton = driver.find_element(By.XPATH,
                                                 "/html/body/div[2]/div[3]/div[1]/div[1]/button")
                joinButton.click()
            except:
                break

        try:
            if mode == 2:
                if not driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
                    arrayOfWords = []
                    syllable = driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[2]/div[2]/div").text
                    answerBox = driver.find_element(By.XPATH,
                                                    "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
                    var = syllable

                    for line in stringone.splitlines():
                        if var in line:
                            arrayOfWords.append(line)

                    matchingWord = arrayOfWords[random.randint(0, len(arrayOfWords))]
                    answerBox.click()
                    time.sleep(int(pauseBetween) / 10)
                    for character in matchingWord:
                        characterCode = ord(character) + random.randint(1, 4)
                        randomChance = random.randint(1, 100)

                        if randomChance > chance:
                            fail = False
                        else:
                            fail = True
                        if fail:  # Spelling mistakes algorithm
                            answerBox.send_keys(chr(characterCode))
                            time.sleep(random.randint(2, 5) / 100)
                            time.sleep(0.1)
                            answerBox.send_keys(Keys.BACK_SPACE)
                            time.sleep(0.1)
                            answerBox.send_keys(character)
                        elif not fail:
                            answerBox.send_keys(character)
                        if int(pauseBetween) != 0:
                            time.sleep(int(pauseBetween) / 100)
                    answerBox.send_keys(Keys.RETURN)
                    if extraInfo == 1:
                        print("Sent word", matchingWord)
                    time.sleep(0.01)
            elif mode == 1:
                if not driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():
                    arrayOfWords = []
                    syllable = driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[2]/div[2]/div").text
                    answerBox = driver.find_element(By.XPATH,
                                                    "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
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
                    time.sleep(0.05)
        except:
            pass

runBot()
sys.exit()