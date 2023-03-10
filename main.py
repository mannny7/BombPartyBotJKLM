import os
import random
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


from colorama import just_fix_windows_console
from termcolor import colored

just_fix_windows_console()

sent_words = []


def choose_word(syllable):
    global sent_words
    matches = []
    repeats = 0

    for word in words:
        if syllable in word:
            matches.append(word)

    word_is_repeated = True
    while word_is_repeated:
        if settings["mode"] != 0:
            matches = matches.sort(key=len)
            if settings["mode"] == 1:
                choice = matches[repeats]
            else:
                choice = matches[-1 - repeats]

        else:
            choice = random.choice(matches)

        if not (choice in sent_words):
            word_is_repeated = False

    choice = ''.join(choice)
    sent_words.append(choice)

    if settings["print_all_matches"]:
        log(matches)

    return choice


def log(string, color="green"):
    final = ">>> " + str(string)
    print(colored(final, color))


log(""" 
    _____  __    __  __        __       __        _______    ______   ________ 
   /     |/  |  /  |/  |      /  \     /  |      /       \  /      \ /        |
   $$$$$ |$$ | /$$/ $$ |      $$  \   /$$ |      $$$$$$$  |/$$$$$$  |$$$$$$$$/ 
      $$ |$$ |/$$/  $$ |      $$$  \ /$$$ |      $$ |__$$ |$$ |  $$ |   $$ |   
 __   $$ |$$  $$<   $$ |      $$$$  /$$$$ |      $$    $$< $$ |  $$ |   $$ |   
/  |  $$ |$$$$$  \  $$ |      $$ $$ $$/$$ |      $$$$$$$  |$$ |  $$ |   $$ |   
$$ \__$$ |$$ |$$  \ $$ |_____ $$ |$$$/ $$ |      $$ |__$$ |$$ \__$$ |   $$ |   
$$    $$/ $$ | $$  |$$       |$$ | $/  $$ |      $$    $$/ $$    $$/    $$ |   
 $$$$$$/  $$/   $$/ $$$$$$$$/ $$/      $$/       $$$$$$$/   $$$$$$/     $$/    
                                                                                                   """)

log("Welcome to Manny's JKLM bot \n    Change settings by opening the JSON file located in the same folder as the "
    "script \n    Discord: Manny.#0001")
selfPass = input(colored(">>> Press enter to continue... ", "red"))

fileLocation = os.path.dirname(os.path.realpath(__file__))

# Load the settings
settings = json.load(open(fileLocation + "/settings.json"))
if settings["debug"]:
    log(settings, color="red")


# Open the text file for all the words
words = []
with open(fileLocation + "\\wordlist", "r") as file:
    for line in file:
        words.append(line[:len(line) - 1])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.jklm.fun")

while True:
    while True:
        try:
            driver.switch_to.frame(
                driver.find_element(By.XPATH,
                                    "//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))
        except:
            break

    while True:
        try:
            joinButton = driver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[3]/div[1]/div[1]/button")

            time.sleep(settings["delay_before_joining"])
            joinButton.click()

        except:
            break

    try:

        if not driver.find_element(By.XPATH,
                                   "/html/body/div[2]/div[3]/div[2]/div[1]").is_displayed():

            print("it's ur turn bruh")
            # Will return True if it is our turn
            matches = []

            syllable = driver.find_element(By.XPATH,
                                           "/html/body/div[2]/div[2]/div[2]/div[2]/div").text
            answerBox = driver.find_element(By.XPATH,
                                            "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

            word_to_send = choose_word(syllable)

            answerBox.click()
            for char in word_to_send:
                answerBox.send_keys(char)
                time.sleep(settings["delay_between_typing"])

            if settings["automatically_send_words"]:
                answerBox.send_keys(Keys.RETURN)

            if settings["print_word_sent"]:
                log("Sent word" + " " + word_to_send)
    except:
        pass
