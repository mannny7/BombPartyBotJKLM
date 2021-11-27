import json
import os
import random
import sys
import time

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import *
from selenium import webdriver
from selenium.webdriver.chrome import service as cs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Home")
main_win.resize(300, 100)


def settings0():
    button0.show()
    label1.setText("Choose a mode: ")
    main_win.setWindowTitle("Setting up")
    button0.hide()
    button1.setText("Continue")
    button3.show()
    button2.show()
    label1.show()
    button1.clicked.disconnect()
    button1.clicked.connect(settings1)


def settings1():
    if button2.isChecked():
        main_win.mode = 1
        settings2()
    elif button3.isChecked():
        main_win.mode = 2
        settings2()


def settings2():
    button0.show()
    main_win.setWindowTitle("Almost done")
    label1.setText("Would you like to receive extra info in the console?: ")
    button1.setText("Continue")
    button2.hide()
    button3.hide()
    button4.show()
    button5.show()
    label1.show()
    button1.clicked.disconnect()
    button1.clicked.connect(settings3)


def settings3():
    if button5.isChecked():
        main_win.extraInfo = 2
    elif button4.isChecked():
        main_win.extraInfo = 1
    settings = {
        "chance": main_win.chance,
        "pause": main_win.pauseBetween,
        "begin": main_win.timeBeforeType,
        "mode": main_win.mode,
        "info": main_win.extraInfo
    }
    with open("settings.json", "w") as file:
        json.dump(settings, file, ensure_ascii=False)
    import bot.py

def humanSettings():
    label1.hide()
    button4.hide()
    button5.hide()
    button0.setText("Back")
    button1.hide()
    button8.show()
    timeBeforeTyping()
    label2.show()
    label5.show()
    label3.show()
    main_win.setWindowTitle("Human-like settings")
    slider1.show()
    slider1.valueChanged.connect(timeBeforeTyping)
    label4.show()
    slider2.show()
    slider2.valueChanged.connect(pauseBetweenChar)
    label6.show()
    slider3.show()
    label7.show()
    slider3.valueChanged.connect(failChance)
    button8.clicked.connect(home)
    button0.clicked.connect(home)


def timeBeforeTyping():
    main_win.timeBeforeType = slider1.value()
    label2text = int(main_win.timeBeforeType) / 10
    label2final = str(label2text) + "s"
    label2.setText(label2final)


def pauseBetweenChar():
    main_win.pauseBetween = slider2.value()
    label5text = int(main_win.pauseBetween) / 100
    label5final = str(label5text) + "s"
    label5.setText(label5final)


def failChance():
    main_win.chance = slider3.value()
    label6final = str(main_win.chance) + "%"
    label6.setText(label6final)


def home():
    main_win.resize(300, 100)
    main_win.setWindowTitle("Home")
    label6.hide()
    label7.hide()
    slider3.hide()
    button8.hide()
    label5.hide()
    label2.hide()
    label3.hide()
    label4.hide()
    slider1.hide()
    slider2.hide()
    button0.show()
    button2.hide()
    button3.hide()
    button4.hide()
    button5.hide()
    label1.hide()
    button1.setText("Run bot")
    button1.show()
    button0.setText("Settings")
    button1.clicked.disconnect()
    button0.clicked.disconnect()
    button1.clicked.connect(settings0)
    button0.clicked.connect(humanSettings)


main_win.chance = 50
main_win.pauseBetween = 25
main_win.timeBeforeType = 15

main_win.mode = 0
main_win.extraInfo = 0
RadioGroup = QButtonGroup()

button0 = QPushButton("Settings")
button1 = QPushButton("Run bot")
button2 = QRadioButton("Blatant")
button3 = QRadioButton("Human-like")
button4 = QRadioButton("Yes")
button5 = QRadioButton("No")
button8 = QPushButton("Save changes")

slider1 = QSlider(Qt.Horizontal)
slider1.setMaximum(20)
slider1.setMinimum(10)
slider1.setValue(15)
slider1.setTickPosition(QSlider.TicksBelow)
slider1.setTickInterval(1)
slider2 = QSlider(Qt.Horizontal)
slider2.setMaximum(100)
slider2.setMinimum(0)
slider2.setValue(25)
slider2.setTickPosition(QSlider.TicksBelow)
slider2.setTickInterval(5)
slider3 = QSlider(Qt.Horizontal)
slider3.setMaximum(100)
slider3.setMinimum(0)
slider3.setValue(50)
slider3.setTickPosition(QSlider.TicksBelow)
slider3.setTickInterval(10)
label1 = QLabel("Choose mode:")
label2 = QLabel("1.5s")
label3 = QLabel("Choose how long the bot pauses in seconds before typing")
label4 = QLabel("Choose the pause between characters in seconds")
label5 = QLabel("0.25")
label6 = QLabel("50%")
label7 = QLabel("Choose the percent chance of the bot making an \"error\" whilst typing")
label3.hide()
label1.hide()
button2.hide()
button3.hide()
button4.hide()
button5.hide()
slider1.hide()
slider2.hide()
slider3.hide()
label4.hide()
label2.hide()
label5.hide()
label6.hide()
label7.hide()
button8.hide()
vline1 = QVBoxLayout()

RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
RadioGroup.addButton(button5)

vline1.addWidget(button0)
vline1.addWidget(label1)
vline1.addWidget(button3)
vline1.addWidget(button2)
vline1.addWidget(button4)
vline1.addWidget(button5)
vline1.addWidget(button1)
vline1.addWidget(label3)
vline1.addWidget(slider1)
vline1.addWidget(label2)
vline1.addWidget(label4)
vline1.addWidget(slider2)
vline1.addWidget(label5)
vline1.addWidget(label7)
vline1.addWidget(slider3)
vline1.addWidget(label6)
vline1.addWidget(button8)

button0.setFixedWidth(60)
button0.clicked.connect(humanSettings)
button1.clicked.connect(settings0)
main_win.setLayout(vline1)
main_win.show()
app.exec()
