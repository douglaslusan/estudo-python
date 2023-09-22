import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# importando arquivos CSV
vendas_df = pd.read_csv(r'Vendas  - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Clientes.csv', sep=';')

# limpando colunas desnecessarias
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Categoria']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'Email Cliente'})

# frequencia_cliente = vendas_df['Email Cliente'].value_counts()
#
# frequencia_cliente[:5].plot(figsize=(15, 5))


vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]

vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending=False)

vendas_lojas[:5].plot(figsize=(16, 8), kind='bar')

print(vendas_lojas[:5])
maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_valor = vendas_lojas['Quantidade Vendida'].idxmax()

print(maior_valor)
print(melhor_valor)
print(vendas_lojas[-1:])




plt.show()

plt.close()
