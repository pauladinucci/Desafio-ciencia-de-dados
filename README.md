# Desafio de Ciência de Dados - Indicium
<div>Desafio de ciência de dados da empresa indicium com objetivo de testar conhecimento de resolulçai de problemas de análise de dados e aplicações de modelos preditivos.
<br>
<br>
Este desafio tem como objetivo identificar quais máquina apresentam potencial de falha com base em dados extraídos através de sensores durante o processo de manufatura utilizlando dois datasets: desafio_manutencao_preditiva_treino e desafio_manufatura_preditiva_teste. Tendo como objetivo prever a coluna "failure_type" no dataset referente ao desaio_manufatura_preditiva_teste a partir dos dados.
</div>
<div>
Para responder a esta entrega, foram feitas as seguintes especificações:
<br>
<br>
1)Descreva graficamente os dados disponíveis, apresentando as principais estatísticas descritivas. Comente o porquê da escolha dessas estatísticas.

2)Explique como você faria a previsão do tipo de falha a partir dos dados. Quais variáveis e/ou suas transformações você utilizou e por quê? Qual tipo de problema estamos resolvendo (regressão, classificação)? Qual modelo melhor se aproxima dos dados e quais seus prós e contras? Qual medida de performance do modelo foi escolhida e por quê?

3)Envie o resultado final do modelo em uma planilha com apenas duas colunas (rowNumber, predictedValues). 

4)A entrega deve ser feita através de um repositório de código público que contenha:
a.README explicando como rodar o projeto

b.Arquivo requirements com todos os pacotes utilizados.

c.Relatório de EDA em PDF, Jupyter Notebook ou semelhante conforme passo 1

d.Códigos de modelagem utilizados no passo 2.

e.Arquivo final predicted.csv conforme passo 3 acima.
</div>
<div>
A previsão do tipo de falha foi feita utilizando random forest (ou árvore aleatória), criando árvores de decisão de maneira aleatória onde cada árvore será utilizada no resultado final, em uma espécie de votação.
Se estabelecem regras para tomada de decisão nas quais o algoritmo cria uma estutura similar a um fluxograma aonde uma condição é verificada, se atendida o fluxo segue por um ramo, caso contrário, por outro, sempre levando o próximo nó, até a finalixação da árvore.
Com os dados de treino, o algoritmo busca as melhores condições e onde inserir cada uma dentro do fluxo.
O primeiro passo executado no algoritmo será selecionar aleatoriamente algumas amostras dos dados de treino, não sua totalidade. É utilizado o bootstrap, que é um método de reamostragem onde as amostras são repetidas na seleção. Com esta primeira seleção de amostras será construída a árvore de decisão.

#2-como foi feita a previsao do tipo de falhas(random forest), tranformações de dados feitas e qual tipo de problema? Classificação, pros e contras do modelo. medidas de performance(acuracia e precision)


</div>
