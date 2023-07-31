import sys


def txt_importer(file_path):
    mensagem_erro_formato_invalido = "Formato inválido"
    mensagem_erro_arquivo_nao_encontrado = "Arquivo {file_path} não encontrado"

    if not file_path.endswith(".txt"):
        sys.stderr.write(mensagem_erro_formato_invalido + "\n")
        return []

    try:
        with open(file_path, "r") as file:
            result = file.read().splitlines()
            return result
    except FileNotFoundError:
        sys.stderr.write(mensagem_erro_arquivo_nao_encontrado.format(file_path=file_path) + "\n")
        return []
