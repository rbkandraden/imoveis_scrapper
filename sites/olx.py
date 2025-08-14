from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar_imoveis_olx(cidade="rio de janeiro", estado="rj", max_preco=5000):
    url = f"https://{estado}.olx.com.br/regiao-de-{cidade}/imoveis/aluguel/apartamentos?pe={max_preco}&q=2%20quartos"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    time.sleep(5)

    resultados = []

    try:
        anuncios = driver.find_elements(By.CSS_SELECTOR, "li.sc-1fcmfeb-2")
        for anuncio in anuncios:
            try:
                titulo = anuncio.find_element(By.CLASS_NAME, "sc-1fcmfeb-6").text
                preco = anuncio.find_element(By.CLASS_NAME, "sc-ifAKCX").text
                link = anuncio.find_element(By.TAG_NAME, "a").get_attribute("href")
                detalhes = anuncio.text

                preco_valor = int(''.join(filter(str.isdigit, preco)))
                if preco_valor <= max_preco * 100:
                    if "2 quarto" in detalhes.lower() or "2 dorm" in detalhes.lower():
                        resultados.append({
                            "titulo": titulo,
                            "preco": preco,
                            "link": link,
                            "descricao": detalhes
                        })
            except Exception:
                continue
    finally:
        driver.quit()

    return resultados

if __name__ == "__main__":
    imoveis = buscar_imoveis_olx()
    for imovel in imoveis:
        print(imovel)
