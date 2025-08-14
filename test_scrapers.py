
from sites.olx import buscar_imoveis_olx
from sites.zap import buscar_imoveis_zap
from sites.vivareal import buscar_imoveis_vivareal
# Supondo que você tenha um scraper para o QuintoAndar:
# from sites.quintoandar import buscar_imoveis_quintoandar

scrapers = [
    buscar_imoveis_olx,
    buscar_imoveis_zap,
    buscar_imoveis_vivareal,
    # buscar_imoveis_quintoandar,  # Descomente se/quando existir
]

def test_scrapers():
    for scraper in scrapers:
        resultados = scraper("petrolina", "pe")
        assert isinstance(resultados, list), f"{scraper.__name__} não retornou uma lista"
        if resultados:
            item = resultados[0]
            assert isinstance(item, dict), f"{scraper.__name__} não retornou dicionários"
            assert "titulo" in item or "preco" in item, f"{scraper.__name__} não retornou campos esperados"
