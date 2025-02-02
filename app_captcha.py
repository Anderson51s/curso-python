# Reconhecimento de imagem captcha
import pyautogui
import pyscreeze
from PIL import image

captcha = pyautogui.locateOnScreen('google_captcha.png')
pyautogui.click(captcha[0],captcha[1],duration=2)
