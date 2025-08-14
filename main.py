
from sites.olx import buscar_imoveis_olx
from sites.zap import buscar_imoveis_zap
from sites.vivareal import buscar_imoveis_vivareal

from utils import salvar_em_excel


def main():
    cidade = "petrolina"
    estado = "pe"
    todos = []

    scrapers = [
        buscar_imoveis_olx,
        buscar_imoveis_zap,
        buscar_imoveis_vivareal,
        # Adicione aqui buscar_imoveis_quintoandar quando implementar
    ]

    for scraper in scrapers:
        try:
            resultados = scraper(cidade, estado)
            print(f"✅ {scraper.__name__}: {len(resultados)} imóveis")
            todos.extend(resultados)
        except Exception as e:
            print(f"❌ Erro em {scraper.__name__}: {e}")

    if todos:
        salvar_em_excel(todos, "apt2q_ate800_petrolina.xlsx")
    else:
        print("⚠️ Nenhum imóvel encontrado em nenhum site.")


if __name__ == "__main__":
    main()
