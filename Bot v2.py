import cv2 as cv
import numpy as np
import pyautogui
import pydirectinput
import keyboard
import time
import os

car = 'lfa'

#pyautogui.displayMousePosition()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pydirectinput.moveTo(1804, 14)
pydirectinput.mouseDown()
pydirectinput.mouseUp()

def botao_buscar():
    pydirectinput.moveTo(436, 369)
    pydirectinput.press('enter', presses=4)
    
def reconhece_carro():
    time.sleep(0.5)
    pyautogui.screenshot('.//capture//captureCar.jpg', region=(110, 300, 205, 130))

    capture_car = cv.imread('.//capture//captureCar.jpg', cv.IMREAD_UNCHANGED)
    source_car = cv.imread(f'.//cars//{car}.jpg', cv.IMREAD_UNCHANGED)
    resultado_car = cv.matchTemplate(capture_car, source_car, cv.TM_CCOEFF_NORMED)
    limite_car = 0.62
    car_busca = np.where(resultado_car >= limite_car)
    car_busca = list(zip(*car_busca[::-1]))
   
    if car_busca:
        print("CARRO")
        os.remove('.//capture//captureCar.jpg')
        pydirectinput.press('y')
        pydirectinput.press('down')
        pydirectinput.press('enter')
        pydirectinput.press('enter')
        pydirectinput.press('enter')
        verifica_compra()    
    else:
        pydirectinput.press('esc')
        time.sleep(0.53) 
    
def verifica_compra():
    time.sleep(3)
    pyautogui.screenshot('.//capture//compraSucedida.jpg', region=(766, 459, 380, 45))

    capture_compra = cv.imread('.//capture//compraSucedida.jpg', cv.IMREAD_UNCHANGED)
    source_compra = cv.imread('.//source//compraIcon.jpg', cv.IMREAD_UNCHANGED)
    resultado_compra = cv.matchTemplate(capture_compra, source_compra, cv.TM_CCOEFF_NORMED)
    limite_compra = 0.6  
    compra_busca = np.where(resultado_compra >= limite_compra)
    compra_busca = list(zip(*compra_busca[::-1]))

    if compra_busca:
        os.remove('.//capture//compraSucedida.jpg')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('esc')
        time.sleep(1)
        pydirectinput.press('esc')
        time.sleep(1)
    else:
        os.remove('.//capture//compraSucedida.jpg')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('esc')
        time.sleep(1)
        pydirectinput.press('esc')
        time.sleep(1)

while True:
    if keyboard.is_pressed('q'):
        os.exit(0)
    botao_buscar()   
    reconhece_carro()
