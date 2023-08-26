import pandas as pd

# Criar um DataFrame vazio
df_empty = pd.DataFrame()

# Criar um DataFrame com dados e índices personalizados
data = {'X': [1, 2], 'Y': [1, 2]}
index = ['Product A', 'Product B']
df_custom = pd.DataFrame(data, index=index)

# Criar uma série
series = pd.Series([1, 2, 3, 4, 5])

# Nomear uma série
series_named = pd.Series([1, 2, 3, 4, 5], name='nome do produto')

# Ler um arquivo CSV
csv_data = pd.read_csv("caminho do arquivo csv")

# Visualizar coluna de um DataFrame
# df['nome da coluna']

# Selecionar linhas por posição
# df.iloc[0] - primeira linha
# df.iloc[0:10] - linhas de 0 a 9

# Selecionar linhas por índices personalizados
# df.loc['Product A']

# Filtrar linhas com base em condições
# df[df['country'] == 'Italy']
# df[(df['country'] == 'Italy') & (df['points'] >= 90)]
# df[df['country'].isin(['Italy', 'France'])]
# df[df['price'].notnull()]
