def exists_word(word, instance):
    result = []

    for i in range(0, len(instance)):
        file = instance.search(i)
        occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for line, text in enumerate(file["linhas_do_arquivo"]):
            if word.casefold() in text.casefold():
                occurrences["ocorrencias"].append({"linha": line + 1})

        if len(occurrences["ocorrencias"]) > 0:
            result.append(occurrences)

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        occurrences = search_word_in_file(word, file)

        if occurrences:
            file_info = create_file_info(word, file, occurrences)
            result.append(file_info)

    return result


def search_word_in_file(word, file):
    occurrences = []

    for line_n, line_c in enumerate(file["linhas_do_arquivo"], start=1):
        if word.casefold() in line_c.casefold():
            occurrence = {
                "linha": line_n,
                "conteudo": line_c
            }
            occurrences.append(occurrence)

    return occurrences


def create_file_info(word, file, occurrences):
    file_info = {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": occurrences
    }
    return file_info
