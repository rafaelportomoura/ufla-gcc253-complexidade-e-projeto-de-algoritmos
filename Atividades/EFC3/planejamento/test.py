import os
import sys


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

    for aux in range(0, list_len):
        array[end] = aux_array[end]
        end -= 1


def mergeSort(array, begin, end):
    if begin < end:
        half = int((begin + end) / 2)
        mergeSort(array, begin, half)
        mergeSort(array, half + 1, end)
        merge(array, begin, half, end)
    return array


DIR = sys.argv[1]
verbose = True if len(sys.argv) > 2 and sys.argv[2] == "true" else False


def ls(ext=".in", path=DIR):
    array = []
    ls = os.listdir(path)
    for entry in ls:
        if entry != "ls.exe.stackdump" and ext in entry:
            array.append(int(entry.split(".")[0]))
    return array


dot_in = ls(".in", DIR)
dot_out = ls(".out", DIR)

in_files = mergeSort(dot_in, 0, len(dot_in) - 1)
out_files = mergeSort(dot_out, 0, len(dot_out) - 1)


def log(message, v=verbose):
    if v:
        print(message)


def read(path):
    data = ""

    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as f:
            data = f.read()

    return data


def compare(out, alg):
    for i in range(0, len(out)):
        out[i] = out[i].replace(" ", "").replace("\t", "")
        log(f"{out[i]} == {alg[i]} : { '✅' if out[i] == alg[i] else '❌'}")
        if out[i] != alg[i]:
            return "❌"

    return "✅"


os.system("g++ planejamento.cpp -Wall -o main.exe")


for i in range(0, len(in_files)):
    n_in = in_files[i]
    n_out = out_files[i]
    log("\n🚀")
    log(f"Teste in({n_in}) out({n_out})\n")

    in_path = f"{DIR}{os.path.sep}{n_in}.in"
    out_path = f"{DIR}{os.path.sep}{n_out}.out"
    out_file = read(out_path).split("\n")

    out = os.popen(f"./main.exe < {in_path}").read().split("\n")

    log(f"Alg out:  {out}")

    result = compare(out_file, out)

    log(f"Teste {n_in} {result}", True)
    log("🔚")