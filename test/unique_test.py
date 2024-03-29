import os
import sys


test = sys.argv[1]
EXE = sys.argv[2]
DIR = sys.argv[3]
VERBOSE = sys.argv[4] == "true" if len(sys.argv) > 4 else False


def verbose(*args):
    if VERBOSE:
        print(*args)


def read(path):
    data = ""

    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as f:
            data = f.read()

    return data


def compare(out, alg):
    if out != alg:
        return f"❌ (expect {out} to equal {alg})"

    return "✅"


out_file = read(f"{DIR}/{test}.out").split("\n")
out = os.popen(f"{EXE} < {DIR}/{test}.in").read().split("\n")
if VERBOSE:
    for o in out:
        verbose(o)

print(f"\nTeste {test}.in")
casos_de_testes = len(out_file)
corretos = 0
for i in range(0, casos_de_testes):
    # out[i] = out[i].replace(" ", "").replace("\t", "")
    result = compare(out_file[i], out[i])
    corretos = corretos + 1 if result == "✅" else corretos
    print(f"\tCaso de teste ({i+1}) = {result}")

print(f"{corretos} casos de testes corretos de um total de {casos_de_testes} casos\n")
