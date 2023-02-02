import os
import sys
from src.algoritmo import Algoritmo,mergeSort

DIR = sys.argv[1]
verbose = True if len(sys.argv) >2 and sys.argv[2] == 'true' else False

def ls(ext=".in", path=DIR):
    array = []
    ls = os.listdir(path)
    for entry in ls:
        if entry != "ls.exe.stackdump" and ext in entry:
            array.append(int(entry.split('.')[0]))
    return array

dot_in = ls('.in',DIR)
dot_out = ls('.out',DIR)

in_files = mergeSort(dot_in,0,len(dot_in)-1)
out_files = mergeSort(dot_out,0,len(dot_out)-1)

def log(message,verbose=True):
    if (verbose):
        print(message)

def read(path):
    data = ''

    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as f:
            data = f.read()

    return data

def compare(out,alg):
    i =0
    j=1
    is_equal = out[i] == alg[i] and out[j] == alg[j]
    test_result =  '✅' if is_equal else '❌'
    log(f'\tout == alg\ni:\t{out[i]} == {alg[i]}\nj:\t{out[j]} == {alg[j]}',verbose)
    return test_result

for i in range(0,len(in_files)):
    n_in = in_files[i]
    n_out = out_files[i]
    log('\n🚀',verbose)
    log(f'Teste in({n_in}) out({n_out})\n',verbose)

    in_path = f'{DIR}{os.path.sep}{n_in}.in'
    out_path =  f'{DIR}{os.path.sep}{n_out}.out'
    out = read(out_path).split(' ')
    in_data = read(in_path).split()
    out = [int(out[0]),int(out[1])]
    
    in_data_int = [int(x) for x in in_data if int(x)]
    

    alg = Algoritmo(in_data_int, verbose)
    alg_out = alg.run()

    result = compare(out, alg_out)
    log(f'Teste {n_in}: {result}')
    log('🔚',verbose)