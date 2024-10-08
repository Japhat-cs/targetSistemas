import pandas as pd

# Função para processar os dados de faturamento
def analisar_faturamento(json_data):
    # Lê os dados da tabela JSON
    df = pd.read_json("dados.json")
    
    # Filtra apenas os dias com faturamento > 0
    dias_com_faturamento = df['valor'][df['valor'] > 0]
    
    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = dias_com_faturamento.min()
    maior_faturamento = dias_com_faturamento.max()
    
    # Calcula a média mensal desconsiderando dias sem faturamento
    media_mensal = dias_com_faturamento.mean()
    
    # Conta o número de dias com faturamento superior à média mensal
    dias_acima_da_media = (dias_com_faturamento > media_mensal).sum()
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

json_data = pd.read_json("dados.json")

menor, maior, dias_acima_media = analisar_faturamento(json_data)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")
