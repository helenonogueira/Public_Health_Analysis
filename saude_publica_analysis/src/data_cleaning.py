
import pandas as pd

df = pd.read_csv('C:\\Users\\Heleno\\Documents\\Projetos Portifólio\\saude_publica_analysis\\data\\World_Development_Indicators.csv')

def clean_data(df):
    # Excluir colunas irrelevantes
    df = df.drop(columns=['Series Name', 'coluna_irrelevante_2'])

    # Tratar valores faltantes
    df['taxa_mortalidade'] = df['taxa_mortalidade'].fillna(df['taxa_mortalidade'].mean())

    # Converter colunas de ano
    df['ano'] = pd.to_datetime(df['ano'], format='%Y')

    return df
