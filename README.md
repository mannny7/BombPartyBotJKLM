# BombPartyBotJKLM
A simple bot for Bomb Party on https://www.jklm.fun

Features include:

1. Auto join games
2. Auto answer prompts
3. Human-like spelling mistakes
4. Custom typing speed

Sorry if some code is poorly wrote I'm quite new to Python and only 13 :)

<h1>A guide to downloading, running and using:</h1>

1. Download a zip of the code
2. Extract the zip file
3. Ensure you have Selenium Chrome Webdrivers installed, the application is already in there so it should be fine (DO NOT RUN chromedriver.exe IT DOES NOTHING)
4. If you have an errors along the lines of ```No module named keyboard``` run ```pip install (missing module)``` in command prompt. Obviously replace (missing module) with the module name. If you don't have pip installed run ```py -m ensurepip --upgrade``` if that is ```Not recognised as an internal or external command``` ensure you have python itself installed (https://www.python.org/downloads/) and if you do have python installed, install it anyway and follow the steps below:

![image](https://user-images.githubusercontent.com/38955706/127909526-92be09d7-61a2-4c2a-a1e7-99a2c34472a8.png)

Upon the installer running click on ```Customize installation``` 

![image](https://user-images.githubusercontent.com/38955706/127909570-d6a4eccc-b90e-4813-8680-617e91382bb0.png)

Press ```Next```

![image](https://user-images.githubusercontent.com/38955706/127909596-95b8bbdd-3137-4c7c-bb67-0556a9d65e24.png)

And make sure ```Add Python to Environment Variables``` is selected. If it is not tick it and press ```Install``` if it is ticked further troubleshooting is required, DM me on discord Mannnny#5377 or open an issue.

Here is a YouTube video for more help https://youtu.be/N5b6sALTN7g
<h1>On line 17 change the path variable to the path that your code is located (add /web2 on the end) >>>IMPORTANT<<<</h1>

Here is how to do that:
![image](https://user-images.githubusercontent.com/38955706/127859142-f363944b-596e-4bf8-af3f-1e72e0018ad7.png)
Find where the file is downloaded and click on the path at the top

![image](https://user-images.githubusercontent.com/38955706/127859219-bcf45f8f-e857-4d45-8fc8-592fa64225df.png)

This will highlight the text, copy it and paste it into the code

![image](https://user-images.githubusercontent.com/38955706/127859322-0540be37-400e-486b-9b94-73e507319dde.png)

Now simply swap all the backslashes for forward slashes

![image](https://user-images.githubusercontent.com/38955706/127859421-3c2c1612-0813-4a41-a885-8a12598e0c05.png)

And finally add /web2 on the end so the program can find the file

![image](https://user-images.githubusercontent.com/38955706/127859545-352c2dfc-5ef2-4747-ae4a-8d0668b6b479.png)

Now there shouldn't be any errors. MAKE SURE THE PATH HAS "" OR '' ON EITHER SIDE

<h1>Using the bot:</h1>

When the webpage opens simply join any game of Bomb Party and wait for the round to end, the bot should auto join in the next round and start playing!
You don't need to press anything the code runs automatically upon it changing to your turn, however pressing and holding 'z' will end the code incase anything goes wrong you can change this hotkey on line 23

![image](https://user-images.githubusercontent.com/38955706/127860112-3711e73f-2af9-4e2a-85df-06c2c8526882.png)

Change the 'z' to whatever your heart desires but remember quotation marks on either side!

  <h1>Customization!</h1>
  
If you're not happy with how somethings working (for example the typing speed or the amount of mistakes) here is how to change them!
  <h3>Typing speed:</h3>
  
To change the typing speed change the parameters on line 70 the program chooses a random number between the lower and upper number divides by 100 and thats is the pause between each letter so having a lower number of five and an upper of six means to bot will type with a delay of 0.06 seconds of 0.05 seconds between each letter! Make sure they are seperated by a comma and don't use decimals
  
  ![image](https://user-images.githubusercontent.com/38955706/127861299-1d59f4d2-c4bf-4f6e-a5a5-24b29e7d897d.png)
  
If you use a larger range for the parameters it looks more realistic as if you're stopping to think
  
  <h3>Amount of mistakes:</h3>
Again if you're not happy with the amount of mistakes the bot is making change the parameters on line 53 for the variable "fail" this is the chance of a character "failing" the higher the range between the paramters the less mistakes. Think of it like a fraction. By default it is set to a 1 in 12 chance so every letter has a 1 in 12 chance to "fail". Change this to whatever you want, make sure they are whole numbers.
  
  ![image](https://user-images.githubusercontent.com/38955706/127861667-9dd3550f-a307-4ecb-8158-3471da284cd4.png)

  <h3>Changing mistakes themselves:</h3>
  
If you're unhappy with the "fails" themselves you can customize how many random letters are produced and then deleted! For this one go to line 55 and change the parameters. I recommend keeping the lower parameter as 1 but set the top paramter as high as you want (the higher the less realistic)
 
  ![image](https://user-images.githubusercontent.com/38955706/127862010-abb4ef51-7923-45bc-82b1-3e63ca6e9fec.png)
  <h3> How fast mistakes are written:</h3>
  
As well as this you can change how fast the random letters during a fail are typed this is found on line 59 and refer to changing the typing speed to find out what this means.
  
  ![image](https://user-images.githubusercontent.com/38955706/127862184-a798c682-ff15-463f-9284-833b565628b4.png)

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

https://youtu.be/N5b6sALTN7g YouTube video for installing help
