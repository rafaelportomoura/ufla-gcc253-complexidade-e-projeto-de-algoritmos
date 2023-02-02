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
        self.fornecedores = mergeSort(self.fornecedores,0,len(self.fornecedores)-1)
        
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
