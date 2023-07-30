from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC =  ROOT_FOLDER / "driver" / 'chromedriver.exe'

def make_chorme_driver(*opcoes: str) -> webdriver.Chrome:
    
    opcoes_chrome = webdriver.ChromeOptions()

    if opcoes_chrome is not None:
        for opcao in opcoes:
            opcoes_chrome.add_argument(opcao)

    chrome_service = Service(executable_path=CHROMEDRIVER_EXEC)

    opcoes_chrome.add_argument("--start-maximized")
    chrome_driver  = webdriver.Chrome(
        service=chrome_service,
        options=opcoes_chrome
    )

    return chrome_driver


if __name__ =='__main__':
    driver = make_chorme_driver('--start-maximized')
    driver.get('https://github.com/')
    TIME_TO_WAIT = 10

    try:

        # Esperar para encontrar
        botao_login = WebDriverWait(driver, TIME_TO_WAIT).until(
            # Passando condição
            ec.presence_of_element_located(
                (By.LINK_TEXT, "Sign in")
            )
        )

        botao_login.click()

    except:
        print("Não foi possível encontrar o elemento!")
    
    try:
        # Esperar para encontrar
        nome_usuario = WebDriverWait(driver, TIME_TO_WAIT).until(
            # Passando condição
            ec.presence_of_element_located(
                (By.ID, "login_field")
            )
        )

        nome_usuario.send_keys("USUARIO AQUI")

        # Esperar para encontrar
        senha_usuario = WebDriverWait(driver, TIME_TO_WAIT).until(
            # Passando condição
            ec.presence_of_element_located(
                (By.ID, "password")
            )
        )

        senha_usuario.send_keys("SENHA AQUI")

        # Esperar para encontrar
        botao_logar = WebDriverWait(driver, TIME_TO_WAIT).until(
            # Passando condição
            ec.presence_of_element_located(
                (By.NAME, "commit")
            )
        )

        botao_logar.send_keys(Keys.ENTER)
    except:
        pass
    
    # outra forma de buscar elementos
    # botaoX = driver.find_element(By.ID, "nome id")

    sleep(10)
    