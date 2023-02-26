import os
import sys

os.system("g++ planejamento.cpp -Wall -o main.exe")

test = sys.argv[1]

os.system(f"./main.exe < test/{test}.in")


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


out_file = read(f"test/{test}.out").split("\n")
out = os.popen(f"./main.exe < test/{test}.in").read().split("\n")

print(f"\nTeste {test}.in")
casos_de_testes = len(out_file)
corretos = 0
for i in range(0, casos_de_testes):
    out[i] = out[i].replace(" ", "").replace("\t", "")
    result = compare(out_file[i], out[i])
    corretos = corretos + 1 if result == "✅" else corretos
    print(f"\tCaso de teste ({i}) = {result}")

print(f"{corretos} casos de testes corretos de um total de {casos_de_testes} casos\n")