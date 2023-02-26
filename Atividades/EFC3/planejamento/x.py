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
                write(data, file, retry - 1)
            else:
                print("Arquivo não existe!")
    except Exception as e:
        print(f"Não foi possível escrever!\nArquivo: {file}")


x = read("test/1.in").split("JACARE")
o = read("test/1.out").split("\n")

file = 3
i = 0
for y in x:
    write(f"test/{file}.in", y)
    write(f"test/{file}.out", o[i])
    file += 1
    i += 1
    if file % 2:
        r = input(f"{file}: Ok?")
        if r == "n" or r == "N":
            exit(0)
