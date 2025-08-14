from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar_imoveis_vivareal(cidade="rio de janeiro", estado="rj", max_preco=5000):
    url = "https://www.vivareal.com.br/aluguel/rj/rio-de-janeiro/zona-sul/apartamento_residencial/com-mobiliado/?onde=%2CRio+de+Janeiro%2CRio+de+Janeiro%2CZona+Sul%2C%2C%2C%2Ccity%2CBR%3ERio+de+Janeiro%3ENULL%3ERio+de+Janeiro%3EZona+Sul%2C-22.906847%2C-43.172897%2C&tipos=apartamento_residencial%2Ckitnet_residencial&amenities=Mobiliado&quartos=1%2C2&precoMaximo=5000&precoTotal=true&proximoMetro=true&transacao=aluguel"

    options = Options()
    options.add_argument("--headless")  # Opcional: executa sem abrir janela do navegador
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)  # aguarda carregamento da página

    resultados = []

    try:
        anuncios = driver.find_elements(By.CSS_SELECTOR, '[data-type="property"]')
        for anuncio in anuncios:
            try:
                titulo = anuncio.find_element(By.CSS_SELECTOR, "span.property-card__title").text
                preco = anuncio.find_element(By.CSS_SELECTOR, "div.property-card__price").text
                link = anuncio.find_element(By.TAG_NAME, "a").get_attribute("href")
                descricao = anuncio.find_element(By.CSS_SELECTOR, ".property-card__address").text

                preco_valor = int(''.join(filter(str.isdigit, preco)))
                if preco_valor <= max_preco * 100:
                    resultados.append({
                        "titulo": titulo,
                        "preco": preco,
                        "link": link,
                        "descricao": descricao
                    })
            except Exception:
                continue

    finally:
        driver.quit()

    return resultados

if __name__ == "__main__":
    imoveis = buscar_imoveis_vivareal()
    for imovel in imoveis:
        print(imovel)
