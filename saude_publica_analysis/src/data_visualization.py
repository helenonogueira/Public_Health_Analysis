
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
import plotly.express as px
import pandas as pd

df = pd.read_csv('../data/who_health_data.csv')

def plot_mortalidade_distribution(df):
    plt.figure(figsize=(10,6))
    sns.histplot(df['taxa_mortalidade'], kde=True)
    plt.title('Distribuição da Taxa de Mortalidade')
    plt.show()

def plot_mortalidade_trend(df):
    plt.figure(figsize=(12,6))
    sns.lineplot(x='ano', y='taxa_mortalidade', data=df)
    plt.title('Tendência da Taxa de Mortalidade ao Longo do Tempo')
    plt.show()

def plot_interactive_mortalidade(df):
    fig = px.line(df, x='ano', y='taxa_mortalidade', color='pais', title='Taxa de Mortalidade por País ao Longo do Tempo')
    fig.show()
