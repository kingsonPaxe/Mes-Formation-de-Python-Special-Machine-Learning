import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('/home/jeovanipaxe/Documents/Mes-Formation-de-Python-Special-Machine-Learning/ML Teo Me Why/datasets/dados_frutas.xlsx')
print(df)

y =df['Fruta'] #target - variavel alvo(y), ou seja a variavel que eu quero detetar ou classificar. Onde ela recebe a lista de todas as frutas [Morango, limao, etc...]
print(y)

# Selecionando o modelo
arvore = tree.DecisionTreeClassifier(random_state=42)
# variavel x
x = df[df.columns[:4]] # pegando variaves que serao usadas para calssificar como: [Arredondada,  Suculenta, Vermelha,  Doce]

# ISSO AQUI JÁ É MACHINE LEANiRNG!!!
treino = arvore.fit(x, y)

# PREVENDO QUAL DOS ELEMENTOS CORRESPONDENTE A  [Arredondada,  Suculenta, Vermelha,  Doce] É Morango, Limão,Pera, Banana, Cereja,Tomate ou Maçã
print(treino.predict([[0,0,0,1]]))
