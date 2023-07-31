from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    fila_tamanho = len(instance)
    arquivo_existente = False

    for i in range(fila_tamanho):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            arquivo_existente = True
            break

    if not arquivo_existente:
        file = txt_importer(path_file)
        dictionary = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(dictionary)
        print(dictionary)


def remove(queue):
    if queue.is_empty():
        print("Não há elementos")
    else:
        removed_file = queue.dequeue()
        sys.stdout.write(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(queue, position):
    if position < 0 or position >= len(queue):
        sys.stderr.write("Posição inválida\n")
    else:
        file_info = queue.search(position)
        sys.stdout.write(f"{file_info}\n")
