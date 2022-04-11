#Bibliotecas a importar para cálculos
import pandas as pd
import math
import numpy as np



#Importar as tabelas de dados de Factor Z e de Vendas
data1 = pd.read_excel(r'C:\Users\jeolarte\OneDrive - Grupo Jerónimo Martins\Documents\Forecast\Python excel files\Tabela_Factor_Z.xlsx')
data2 = pd.read_excel(r'C:\Users\jeolarte\OneDrive - Grupo Jerónimo Martins\Documents\Forecast\Python excel files\Vendas.xlsx')
#Dados para comparar no fim o resultado
#media = mean("VendaTotal")
#https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/
#https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean

mediaTotal = np.mean(data2.loc[:,"VendaTotal"])
mediaCorrigida = np.mean(data2.loc[:,"VendaCorrigida"])

print ("A media da Venda Total é: ", round(np.mean(data2.loc[:,"VendaTotal"]),3))
print ("A media da Venda Corrigida é: ", round(np.mean(data2.loc[:,"VendaCorrigida"]),3))

#Escolher o CCL que quero aplicar ao artigo
ccl = float(input('Type ccl'))

#Ver a fila com os dados de CCL e de Factor Z na consola
#https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
RowFiltered = data1[data1["Probabilidade"] == ccl]
print (RowFiltered)

#Escolher a posição da variavel CCl, que neste caso é o Factor Z que estaria sempre na posição [0,0]
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
LinhaEscolhida = RowFiltered.iloc[0,0]
FactorZ = round(LinhaEscolhida,3)
print ("Factor Z é:",FactorZ)

#Calcular Desvio padrão dos dois tipos de vendas
std1 = round(data2 ["VendaTotal"].std(),3)
print ("Desvio da Venda Total é:",std1)

std2 = round(data2 ["VendaCorrigida"].std(),3)
print ("Desvio da Venda Corrigida é:",std2)

#Definir variaveis para o calculo do tempo para a raiz cuadrada
#https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
CicloEntreEntregas = 3
LeadTime = 2
TempoVariabilidade = CicloEntreEntregas + LeadTime
sqrt = round(math.sqrt(TempoVariabilidade),3)
print ("Raíz Cuadrada  do tempo é:",sqrt)

#Definir as 2 equações para calcular o stock de segurança
Equa1 = round(FactorZ * std1 * sqrt,1)
Equa2 = round(FactorZ * std2 * sqrt,1)
print ("Stock de Segurança para vendas totais é:",Equa1)
print ("Stock de Segurança para vendas totais é:",Equa2)

CoberturaSSTotal = round(Equa1 / mediaTotal,3)
CoberturaSSCorrigida = round(Equa2 / mediaCorrigida,3)
print ("A cobertura do SS com vendas totais é", CoberturaSSTotal, " dias")
print ("A cobertura do SS com vendas corrigidas é", CoberturaSSCorrigida, " dias")
