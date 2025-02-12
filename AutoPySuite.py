import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://orquestrador.com.br/login")
    return driver

def esperar_elemento(driver, by, valor, tempo=10):
    return WebDriverWait(driver, tempo).until(EC.presence_of_element_located((by, valor)))

def clicar_elemento(driver, by, valor, tempo=10):
    WebDriverWait(driver, tempo).until(EC.element_to_be_clickable((by, valor))).click()

def realizar_login(driver):
    try:
        esperar_elemento(driver, By.NAME, "email").send_keys("andre.wgns97@gmail.com")
        senha = esperar_elemento(driver, By.NAME, "password")
        senha.send_keys("Malboro123", Keys.ENTER)
    except Exception as e:
        print(f"Erro ao realizar login: {e}")

def selecionar_supermercado(driver):
    try:
        select_element = esperar_elemento(driver, By.NAME, 'where_to_access')
        Select(select_element).select_by_value('loja')
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Erro ao selecionar supermercado: {e}")

def acessar_normatizacao(driver):
    try:
        clicar_elemento(driver, By.CSS_SELECTOR, 'button.btn-primary')
        clicar_elemento(driver, By.CSS_SELECTOR, 'a.nav-link[data-widget="pushmenu"]')
        clicar_elemento(driver, By.CSS_SELECTOR, 'i.fas.fa-palette')
        clicar_elemento(driver, By.XPATH, '//a[contains(@href, "produtos-personalizados")]')
    except Exception as e:
        print(f"Erro ao acessar normatização: {e}")

def incluir_produto(driver):
    try:
        clicar_elemento(driver, By.XPATH, '//a[contains(text(), "Normatizar Produto")]')
        clicar_elemento(driver, By.XPATH, '//*[@id="ModalProdutoPersonalizado"]/div/div/div[2]/a')
    except Exception as e:
        print(f"Erro ao incluir produto: {e}")

def main():
    driver = iniciar_driver()
    realizar_login(driver)
    selecionar_supermercado(driver)
    acessar_normatizacao(driver)
    incluir_produto(driver)
    
    print("Pressione 'Esc' para sair.")
    while not keyboard.is_pressed('esc'):
        time.sleep(1)
    
    driver.quit()
    print("Navegador encerrado.")

if __name__ == "__main__":
    main()
