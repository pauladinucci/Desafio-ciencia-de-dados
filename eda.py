#Os comentários se referem as bibliotecas e códigos referentes a análise das variáveis.


#utilização do sistema
import os
#calculos numericos
import numpy as np 
#manipulacao e analise de dados
import pandas as pd 
#visualizacao de dados
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
#machine learning
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.metrics import f1_score
from sklearn.metrics import precision_score 
from sklearn.metrics import recall_score 
from sklearn.metrics import roc_auc_score #area sob curva roc
from sklearn.metrics import mean_absolute_error, mean_squared_error



#Definindo variaveis principais 
path = "C:/Users/marti/Desktop/Data Science Test" 
os.chdir(path)

train_file = "desafio_manutencao_preditiva_treino.csv"
result_file = "desafio_manutencao_preditiva_teste.csv"


train_set = pd.read_csv(path + "/" + train_file)
result_set = pd.read_csv(path + "/" + result_file)

#Entendendo as variaveis do dataset de treino 
train_set.shape #numero de (linhas, colunas)
train_set.head() #top linhas do arquivo csv
train_set.info() #verificando datatypes de cada coluna do dataset


result_set.shape #numero de (linhas, colunas)
result_set.head() #top linhas do arquivo csv
result_set.info() #verificando datatypes de cada coluna do dataset

train_set.describe() #verificar se existe alguma anomalia ou inconsistencia nos dados
result_set.describe() #verificar se existe alguma anomalia ou inconsistencia nos dados


#criando visualizacao para as metricas do dataset
total_columns = train_set.columns
# definindo variaveis numericas e categoricas para utilizar na viasualizacao dos dados
num_col = train_set._get_numeric_data().columns
describe_train_set = train_set.describe(include=["int64","float64"])
describe_train_set.reset_index(inplace=True)
# remove qualquer variavel do plot
describe_train_set = describe_train_set[describe_train_set["index"] != "count"]
for i in num_col:
    if i in ["index"]:
        continue
    sns.relplot(x= "index", y=i, data=describe_train_set, kind="line")
    plt.savefig(i)
   


