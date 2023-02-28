# Questão 2: Atividades Silviculturais

Uma empresa do setor Florestal, recentemente, procurou uma parceria com um grande centro de pesquisa em Ciência da Computação para resolver a seguinte dor. O setor de silvicultura da empresa enfrenta uma crescente demanda de atividades. Cada atividade i deve ser desenvolvida em um determinado ponto da fazenda, denotado pelas coordenadas cartesianas (xi,yi). Como o tempo de realização de cada atividade é pequeno em relação ao deslocamento da equipe, pode-se desconsiderá-lo na contagem do tempo total gasto. Sabe-se que para deslocar-se do ponto relativo à atividade i para o ponto correspondente à atividade j, a equipe de trabalho gasta uma distância de \* calculada pela distância Euclidiana entre dois pontos. Assume-se que os valores de tempo de deslocamento e distância são proporcionais. A empresa possui um conjunto de n atividades a serem feitas {1,...,n}. Todavia, devido a características de declividade do relevo da fazenda, a rota estabelecida pelos trabalhadores deve iniciar no ponto mais à esquerda do terreno (menor coordenada x), ir da esquerda para a direita, até chegar ao ponto mais à direita. Somente após alcançar tal ponto, a equipe poderá retornar deslocando-se da direita para a esquerda, até alcançar o ponto da extrema esquerda inicial. Todos os pontos de interesse devem ser visitados exatamente uma vez. Seu objetivo é, como membro desse proeminente centro de pesquisa, auxiliar a empresa a encontrar a rota de menor custo, que respeite as características descritas acima. Como custo, considere a distância Euclidiana dos pontos.

## Entradas:

> A entrada do problema consiste em vários casos de teste. A primeira linha de cada caso de teste representa o número de pontos, denotado por n (1 ≤ n ≤ 500). As próximas n linhas indicam as coordenadas (x,y) de cada ponto.

## Saídas:

> A saída de cada caso de teste deve indicar o menor custo obtido, arredondado em uma casa decimal.

_Exemplo de Entrada_:

```txt
7
0 6
5 4
7 5
8 2
6 1
1 0
2 3
3
1 1
2 3
3 1
4
1 1
2 3
3 1
4 2
```

_Exemplo de Saída_:

```txt
25.6
6.5
7.9
```
