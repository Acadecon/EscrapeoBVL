from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui as pg
import pyperclip as pc
import time as t

ruta_driver = "C:\\Program Files (x86)\\chromedriver83.exe"
url_base = "https://www.bvl.com.pe/mercempresas.html"

browser = webdriver.Chrome(ruta_driver)
browser.get(url_base)

t.sleep(3)
pg.hotkey('winleft', 'left')
t.sleep(2)
pg.press('esc')
t.sleep(1)
pg.hotkey('ctrl', 'shift', 'i')
t.sleep(3)
for i in range(3):
    pg.press('up')
pg.hotkey('shift', 'f10')
t.sleep(3)
for i in range(5):
    pg.press('down')
pg.press('right')
for i in range(2):
    pg.press('down')
pg.press('enter')
pg.hotkey('ctrl', 'shift', 'i')
html = pc.paste()
soup = BeautifulSoup(html, "lxml")  # soup es el objeto, lmxl es el parser
with open('html.html', "wb") as file:
    file.write(soup.prettify("utf-8"))
