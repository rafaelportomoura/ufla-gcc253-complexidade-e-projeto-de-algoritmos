# Problema da Escolha de Fornecedores de Papel

A empresa Dunder Mifflin é uma das referências em comercialização de papel, e está com uma nova política de estabelecimento de contrato com seus fornecedores de matéria-prima. Devido à grandes flutuações de preços do mercado, a Dunder Mifflin decidiu que a cada duas semanas, selecionará **dois fornecedores** de matéria-prima cuja a soma dos preços oferecidos para a aquisição de materiais sejam exatamente igual ao orçamento determinado pela Dunder Mifflin.

A Dunder Mifflin é referência mundial no ramo de papel, a recebe diversas propostas de empresas com interesse em firmar parcerias. Diante disso, seu setor de Tecnologia de Informação propôs o seguinte desafio: desenvolva um algoritmo que retorne, a cada duas semanas, quais são os fornecedores escolhidos que respeitem a restrição estabelecida acima.

Detalhe: dado um quantidade de n fornecedores, seu algoritmo deve ter $ O(nlogn) $

## Entrada

Cada caso de teste inicia com o número de fornecedores, indicado por n, em que 2 ≤ n ≤ 10.000. A próxima linha contém n inteiros, representando o preço de venda que cada fornecedor estipula para a encomenda solicitada pela Dunder Mifflin. O preço de venda divulgado por um fornecedor não ultrapassa 1.000.001 unidades monetárias. A próxima linha contem o valor de orçamento da Dunder Mifflin, denotado por B.

## Saída

Imprima o preço dos fornecedores i e j, denotados por pi e pj, tal que pi + pj = B, e pi ≤ pj. Caso hajam múltiplas soluções, a Dunder Mifflin priorizará o preço que minimize pj - pi.

# Algoritmo

## Ordenação

_src/merge_sort.py_

```python
def merge(array, begin, half, end):
    i = begin
    j = half + 1
    aux = begin
    list_len = end - begin + 1
    aux_array = [0] * len(array)

    while i <= half and j <= end:
        if array[i] <= array[j]:
            aux_array[aux] = array[i]
            i += 1
        else:
            aux_array[aux] = array[j]
            j += 1
        aux += 1

    while i <= half:
        aux_array[aux] = array[i]
        i += 1
        aux += 1

    while j <= end:
        aux_array[aux] = array[j]
        j += 1
        aux += 1

    for aux in range(0,list_len):
        array[end] = aux_array[end]
        end -= 1

def mergeSort(array, begin, end):
    if begin < end:
        half = int((begin + end) / 2)
        mergeSort(array, begin, half)
        mergeSort(array, half + 1, end)
        merge(array, begin, half, end)
    return array
```

## Busca

_src/algoritmo.py_

```python
from src.merge_sort import mergeSort

class Algoritmo:
    def __init__(self, in_data, verbose):
        self.n = in_data[0]
        self.fornecedores = []
        for i in range(1,self.n + 1):
            self.fornecedores.append(in_data[i])
        self.orcamento = in_data[-1]
        self.verbose = verbose

    def log(self,message):
        if (self.verbose):
            print(message)

    def run(self):
        self.fornecedores = mergeSort(self.fornecedores)

        return self.busca(self.fornecedores, self.orcamento)

    def busca(self,array,orcamento):
        tam = len(array)
        j = tam - 1
        while (array[j] > orcamento/2):
            j-= 1

        if (array[j] < orcamento/2):
            j+=1

        i = j-1
        self.log(f'i: {i}\tj: {j}')
        while (array[i] + array[j] != orcamento):
            if (array[i] + array[j] > orcamento):
                i-=1
            elif (array[i] + array[j] < orcamento):
                j+=1
        self.log(f'i: {i}\tj: {j}')
        return array[i],array[j]
```

# Executar

## Casos de teste intrínsecos

Casos de teste intrínsecos que estão no diretório `casos_de_teste`  
São 112 casos de teste

```shell
python test.py casos_de_teste
```

## Criar caso de teste

1. crie um diretório
2. dentro dele crie arquivos **{número}.in** para as entradas e **{número}.out** para as saídas
   1. Sendo {número} o número do caso de teste
   2. O {número} de entrada deve ser o mesmo {número} de saída
3. A entrada e saída devem obedecer ao enunciado
   1. caso aja dúvida, pode validar com os casos de teste intrínsecos
4. Obtenha o caminho absoluto ou relativo(a partir da pasta **EFC2/**) para o diretório
   1. substitua `diretorio_de_teste` no comando abaixo pelo caminho
5. Rode o comando

```shell
python test.py diretorio_de_teste
```

## Debugar

O parâmetro `diretorio_de_teste` é o caminho para o diretório contendo os arquivos `.in` e `.out`

```shell
python test.py diretorio_de_teste true
```
