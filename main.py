import os, random, time, json

# So many Selenium imports idk what to do
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from colorama import just_fix_windows_console
from termcolor import colored

# Fix coloured text for Windows console
just_fix_windows_console()

# List of all words sent in the current session to avoid duplicates
sent_words = []

# Choose a word from the word list based of the syllable
def choose_word(syllable):
    global sent_words
    matches = []

    # Number of times a new word has been selected from the current syllable due to duplicates
    repeats = 0

    # Find matching words
    for word in words:
        if syllable in word:
            matches.append(word)

    # If the list isn't empty...
    if matches:
        word_is_repeated = True
        while word_is_repeated:
            if settings["mode"] != 0:
                # Sort the list by length order
                matches = sorted(matches, key=len)
                if settings["mode"] == 1:
                    # If the mode is 1 choose the shortest one
                    choice = matches[repeats]
                else:
                    # If the mode is 2 choose the longest one
                    choice = matches[-1 - repeats]

            else:
                # If the mode is 0 chose a random word
                choice = random.choice(matches)

            # If the word isn't in the already sent list we know it must be a new word so break out of the loop
            if not (choice in sent_words):
                word_is_repeated = False

        choice = ''.join(choice)
        sent_words.append(choice)

    # Print all the matching words according to the settings.json
    if settings["print_all_matches"]:
        log(matches)

    return choice


def log(string, color="green"):
    final = ">>> " + str(string)
    print(colored(final, color))

# Info message
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

# Install the chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.jklm.fun")

while True:
    while True:
        # Switch to the correct iframe for the game
        try:
            driver.switch_to.frame(
                driver.find_element(By.XPATH,
                                    "//div[@class='game']/iframe[contains(@src,'jklm.fun')]"))
        except:
            break

    while True:
        # Click the join button
        try:
            joinButton = driver.find_element(By.XPATH,
                                             "/html/body/div[2]/div[3]/div[1]/div[1]/button")

            # Delay before clicking the button dictated by the settings file
            time.sleep(settings["delay_before_joining"])
            joinButton.click()

        except:
            break

    try:
        matches = []

        # Get the current syllable
        syllable = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[2]/div[2]/div[2]/div").text
        answerBox = driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

        word_to_send = choose_word(syllable)

        answerBox.click()
        for char in word_to_send:
            answerBox.send_keys(char)
            # Small delay between each typed character to make the typing look somewhat human
            time.sleep(settings["delay_between_typing"])

        # Kind of a place holder but maybe make a manual button for sending an answer?
        if settings["automatically_send_words"]:
            answerBox.send_keys(Keys.RETURN)


        # If value is true in the settings folder print the word to send 
        if settings["print_word_sent"]:
            log("Sent word" + " " + word_to_send)
    except:
        pass
