from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar_imoveis_zap(cidade="rio de janeiro", estado="rj", max_preco=5000):
    url = "https://www.zapimoveis.com.br/aluguel/apartamentos/rj+rio-de-janeiro+zona-sul/"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    time.sleep(5)

    resultados = []

    try:
        cards = driver.find_elements(By.CLASS_NAME, "listing-card__content")
        for card in cards:
            try:
                titulo = card.find_element(By.CLASS_NAME, "listing-card__title").text
                preco = card.find_element(By.CLASS_NAME, "listing-card__price").text
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
                descricao = card.find_element(By.CLASS_NAME, "listing-card__address").text

                preco_valor = int(''.join(filter(str.isdigit, preco)))
                if preco_valor <= max_preco * 100:
                    resultados.append({
                        "titulo": titulo,
                        "preco": preco,
                        "link": link,
                        "descricao": descricao
                    })
            except:
                continue
    finally:
        driver.quit()

    return resultados

if __name__ == "__main__":
    imoveis = buscar_imoveis_zap()
    for imovel in imoveis:
        print(imovel)
