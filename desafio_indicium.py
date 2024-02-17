import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

precificacao = pd.read_csv('teste_indicium_precificacao.csv')
df = pd.DataFrame(precificacao)
df