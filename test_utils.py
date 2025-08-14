import os
from utils import salvar_em_excel
import pandas as pd

def test_salvar_em_excel(tmp_path):
    # Dados de exemplo
    lista = [
        {"titulo": "Imóvel 1", "preco": 100000},
        {"titulo": "Imóvel 2", "preco": 200000},
    ]
    arquivo = tmp_path / "test_imoveis.xlsx"
    salvar_em_excel(lista, str(arquivo))
    # Verifica se o arquivo foi criado
    assert arquivo.exists()
    # Verifica se os dados estão corretos
    df = pd.read_excel(arquivo)
    assert len(df) == 2
    assert df.iloc[0]["titulo"] == "Imóvel 1"
    assert df.iloc[1]["preco"] == 200000
