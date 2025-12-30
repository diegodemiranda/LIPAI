"""Aula 01 - Manipulação de Arquivos

Exemplos de operações em arquivos texto: leitura completa, leitura linha a linha,
leitura em lista, escrita e append. Uso seguro com context manager (with).
"""
import os

FILE_PATH = "teste.txt"


def garantir_arquivo_exemplo():
    """Cria um arquivo de exemplo se não existir."""
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write("Primeira linha do arquivo.\nSegunda linha.\nTerceira linha.\n")


def ler_tudo():
    """Lê todo o conteúdo do arquivo e imprime."""
    with open(FILE_PATH, "r", encoding="utf-8") as arquivo:
        print("readable:", arquivo.readable())
        conteudo = arquivo.read()
    print(f"\nRetorna o arquivo lido abaixo:\n{conteudo}")


def ler_primeira_linha_e_lista():
    """Lê a primeira linha e depois todas as linhas em uma lista."""
    with open(FILE_PATH, "r", encoding="utf-8") as arquivo:
        arquivo.seek(0)
        primeira_linha = arquivo.readline()
        print(f"\nLeitura do arquivo na primeira linha -> {primeira_linha.strip()}")

        arquivo.seek(0)
        lista_arquivo = arquivo.readlines()
        print(f"\n\nImprime a lista \n{lista_arquivo}")
    return lista_arquivo


def adicionar_texto(texto):
    """Adiciona texto ao final do arquivo (append)."""
    with open(FILE_PATH, "a", encoding="utf-8") as arquivo:
        print("writable:", arquivo.writable())
        arquivo.write(texto)


def main():
    garantir_arquivo_exemplo()
    ler_tudo()
    _ = ler_primeira_linha_e_lista()

    # adicionar novas linhas
    adicionar_texto("\nC\nRust\n")

    # ler novamente para verificar as alterações
    with open(FILE_PATH, "r", encoding="utf-8") as arquivo:
        nova_lista = arquivo.readlines()
        print(f"\nNova lista gerada\n{nova_lista}")


if __name__ == "__main__":
    main()

