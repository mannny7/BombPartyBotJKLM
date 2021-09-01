# BombPartyBotJKLM
Discord Mannnny#5377

A simple bot for Bomb Party on https://www.jklm.fun

YouTube video for installing: https://youtu.be/IT-0yb12xG0

Features include:

1. Auto join games
2. Auto answer prompts
3. Human-like spelling mistakes
4. Custom typing speed

**Sorry if some code is poorly written I'm quite new to Python and only 13 :)**

<h1>A guide to downloading, running and using:</h1>

1. Download a zip of the code
2. Extract the zip file
3. Ensure you have Selenium Chrome Webdrivers installed, the application is already in there so it should be fine **(DO NOT RUN chromedriver.exe IT DOES NOTHING)**
4. If you have an errors along the lines of ```No module named keyboard``` run ```pip install (missing module)``` in command prompt. Obviously replace (missing module) with the module name. If you don't have pip installed run ```py -m ensurepip --upgrade``` if that is ```Not recognised as an internal or external command``` ensure you have python itself installed (https://www.python.org/downloads/) and if you do have python installed, install it anyway and follow the steps below:

![image](https://user-images.githubusercontent.com/38955706/127909526-92be09d7-61a2-4c2a-a1e7-99a2c34472a8.png)

Upon the installer running click on ```Customize installation``` 

![image](https://user-images.githubusercontent.com/38955706/127909570-d6a4eccc-b90e-4813-8680-617e91382bb0.png)

Press ```Next```

![image](https://user-images.githubusercontent.com/38955706/127909596-95b8bbdd-3137-4c7c-bb67-0556a9d65e24.png)

And make sure ```Add Python to Environment Variables``` is selected. If it is not tick it and press ```Install``` if it is ticked further troubleshooting is required, DM me on discord Mannnny#5377 or open an issue.

Here is a YouTube video for more help https://youtu.be/IT-0yb12xG0
<h1>Using the bot:</h1>

When the webpage opens simply join any game of Bomb Party and wait for the round to end, the bot should auto join in the next round and start playing!
You don't need to press anything the code runs automatically upon it changing to your turn, however pressing and holding 'z' will end the code incase anything goes wrong you can change this hotkey on line 23

![image](https://user-images.githubusercontent.com/38955706/127860112-3711e73f-2af9-4e2a-85df-06c2c8526882.png)

Change the 'z' to whatever your heart desires but remember quotation marks on either side!

  <h1>Bug fixing:</h1>
  
If you run into an issue before the web page even opens make sure you have selenium installed, press Windows + R on your keyboard
  
  ![image](https://user-images.githubusercontent.com/38955706/127863482-327c45f0-7b74-4615-bf9b-61f733358e4a.png)
  
Type in CMD and press enter
  
  ![image](https://user-images.githubusercontent.com/38955706/127863567-f80eb960-240c-4a22-968f-df45f3fcffc8.png)
  
Run ```pip install selenium``` 
  
  ![image](https://user-images.githubusercontent.com/38955706/127863691-96eb5b92-3359-4157-91c6-7e78b55bc8fe.png)

If selenium is not installed it should install it otherwise you'll get a message saying the requirements are satisfied. If selenium is installed and the issue is not covered here open an issue or DM me on discord Mannnny#5377
  
  <h3>Bugs with the bot</h3>
  
  I haven't discovered any bugs with the bot actually playing in a game other than sometimes against StockFish in the first round it will get it wrong but it fixes itself and enters a correct word. If you find any bugs open an issue or DM me on discord Mannnny#5377 and I will work on fixing them. If you have any suggestions or improvements for the bot again just DM me or open an issue.

