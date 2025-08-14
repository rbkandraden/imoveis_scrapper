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
            anuncios = driver.find_elements(By.CSS_SELECTOR, "li.sc-1fcmfeb-2, li.sc-1fcmfeb-1")
            print(f"[OLX] {len(anuncios)} anúncios encontrados na página.")
            for anuncio in anuncios:
                try:
                    try:
                        titulo = anuncio.find_element(By.CLASS_NAME, "sc-1fcmfeb-6").text
                    except:
                        titulo = anuncio.text.split("\n")[0]

                    try:
                        preco = anuncio.find_element(By.CLASS_NAME, "sc-ifAKCX").text
                    except:
                        preco = "N/A"

                    try:
                        link = anuncio.find_element(By.TAG_NAME, "a").get_attribute("href")
                    except:
                        link = ""

                    detalhes = anuncio.text

                    try:
                        preco_valor = int(''.join(filter(str.isdigit, preco)))
                    except:
                        preco_valor = 0

                    if preco_valor <= max_preco * 100:
                        if "2 quarto" in detalhes.lower() or "2 dorm" in detalhes.lower() or "2 qtos" in detalhes.lower():
                            resultados.append({
                                "titulo": titulo,
                                "preco": preco,
                                "link": link,
                                "descricao": detalhes
                            })
                except Exception as e:
                    print(f"[OLX] Erro ao processar anúncio: {e}")
                    continue
        except Exception as e:
            print(f"[OLX] Erro geral: {e}")
        finally:
            driver.quit()

        print(f"[OLX] Total de imóveis coletados: {len(resultados)}")
        return resultados

if __name__ == "__main__":
    imoveis = buscar_imoveis_olx()
    for imovel in imoveis:
        print(imovel)
