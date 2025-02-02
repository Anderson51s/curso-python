import webbrowser
import pyautogui
from time import sleep

# Abrir site no navegador padrao
webbrowser.open('https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_Solicitacao.asp')
# Clicar com mouse na posição - não sou robo
pyautogui.click(1595,530,duration=2)
# Clicar com mouse na posição - CNPJ
pyautogui.click(1164,561,duration=2)
# Digitar CNPJ no campo
pyautogui.typewrite('00.000.000/0001-91')
# Clicar com mouse na posiacao - Consultar
pyautogui.click(1171,640,duration=2)
