#Pegar e arrastar pyautogui
import pyautogui

for i in range(9):
    #mover mouse
    pyautogui.moveTo(1358,257,duration=0.5)
    #clicar arrastar e soltar
    pyautogui.dragTo(1360,790,button='left',duration=0.5)
    # repetir 9 vezes
    