import pandas as pd

try:
    df = pd.read_csv('data/external/retail-sales-dataset.zip')
    print('Dados Carregados com sucesso.')
except FileNotFoundError as file_error:
    print('Erro ao carregador: {}'.format(file_error))

try:
    df.columns = df.columns.str.lower()

    # Coluna 'date' para o tipo datetime
    df['date'] = pd.to_datetime(df['date'])

    # Coluna 'gender' e 'product category' para o tipo category
    df['gender'] = df['gender'].astype('category')

    df['product category'] = df['product category'].astype('category')

    # Adicionar coluna de mês
    df['month'] = df['date'].dt.month
    print('Dados padronizados com sucesso.')
except Exception as general_error:
    print('Ocorreu um erro ao padronizar os documentos: {}.'.format(general_error))

df.to_csv('data/external/dataset.csv', index=False)
