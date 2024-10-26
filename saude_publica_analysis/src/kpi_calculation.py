import pandas as pd

def calculate_kpi_mortalidade(df):
    return df.groupby('pais')['taxa_mortalidade'].mean().reset_index()

def calculate_kpi_expectativa_vida(df):
    return df.groupby('pais')['expectativa_vida'].mean().reset_index()
