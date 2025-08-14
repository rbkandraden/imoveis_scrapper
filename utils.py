import pandas as pd

def salvar_em_excel(lista, arquivo="imoveis.xlsx"):
    df = pd.DataFrame(lista)
    df.to_excel(arquivo, index=False)
    print(f"✅ Salvo {len(df)} imóveis em {arquivo}")
