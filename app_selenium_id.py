# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switchs https://peter.sh/experiments/chromium-command-switches/

    arguments = ['--lang=pt-BR','--window-size=800,600','--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)
    caminho_padrao_para_download = '/home/suportec/Downloads'

    # 
    chrome_options.add_experimental_option("prefs",{
        'download.default_directory': caminho_padrao_para_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/')

botao = driver.find_element(By.ID,'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print('Botão encontrado')
if botoes is not None:
    print('Botões encontrados')
    
input('')
