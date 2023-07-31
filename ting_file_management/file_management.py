import sys


def txt_importer(file_path):
    if not file_path.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return []

    try:
        with open(file_path, "r") as file:
            result = file.read().splitlines()
            return result
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
        return []
