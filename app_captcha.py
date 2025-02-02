# Reconhecimento de imagem captcha
import pyautogui

captcha = pyautogui.locateOnScreen('google_captcha.png')
pyautogui.click(captcha[0],captcha[1],duration=2)
