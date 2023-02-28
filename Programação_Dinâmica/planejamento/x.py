import os


def read(path):
    data = ""

    if os.path.exists(path):
        with open(path, "r", encoding="utf8") as f:
            data = f.read()

    return data


def write(file, data, retry=2):
    try:
        if os.path.exists(file):
            with open(file, "w", encoding="utf8") as f:
                f.write(data)
        else:
            os.system(f"touch {file}")
            if retry > 0:
                write(file, data, retry - 1)
            else:
                print("Arquivo não existe!")
    except Exception as e:
        print(f"Não foi possível escrever!\nArquivo: {file}")


x = read("test/1.in").split("\nJACARE\n")
o = read("test/1.out").split("\n")

file = 3
i = 0

menor = {"file": 3, "motorista": 99, "horas": 99999}

for y in x:
    entrada = y.split("\n")[0]
    [motorista, horas, valor] = entrada.split(" ")

    if (
        menor["motorista"] >= int(motorista)
        and menor["horas"] >= int(horas)
        and motorista != "0"
    ):
        menor["motorista"] = int(motorista)
        menor["horas"] = int(horas)
        menor["file"] = file
        print(menor)
    write(f"test/{file}.in", f"{y}\n0 0 0")
    write(f"test/{file}.out", o[i])
    file += 1
    i += 1
    # if not file % 10:
    #     r = input(f"{file}: Ok?")
    #     if r == "n" or r == "N":
    #         exit(0)
print(f"\nMenor {menor}")
