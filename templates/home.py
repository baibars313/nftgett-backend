from pyclick import HumanClicker
import time 
from PIL import Image
import requests
import pyautogui
# initialize HumanClicker object
URL = "https://cdn.pixabay.com/photo/2022/03/28/22/48/cloudy-7098479_960_720.png"
time.sleep(15)
response = requests.get(URL, stream=True)   # get the picture data from url
image = Image.open(response.raw)            # create a pillow Image from the data
hc=HumanClicker()
x,y=pyautogui.locateCenterOnScreen(image, confidence=0.6, grayscale=True)
hc.move((x,y),.3)