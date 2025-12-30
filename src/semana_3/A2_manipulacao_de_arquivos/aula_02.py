"""Aula 02 - Manipulação de arquivos em Python

Exemplos didáticos de abertura, leitura e escrita de arquivos usando boas práticas
(com context manager). Comentários em português.
"""
from pathlib import Path

ARQUIVO = Path("arquivo_texto.txt")


def criar_arquivo_exemplo():
    """Cria um arquivo de exemplo com algumas linhas, se não existir."""
    if not ARQUIVO.exists():
        ARQUIVO.write_text("Primeira linha do arquivo.\nSegunda linha.\nTerceira linha.\n", encoding="utf-8")


def escrever_simples():
    """Abre o arquivo em modo escrita (w) e escreve uma string."""
    with ARQUIVO.open("w", encoding="utf-8") as arq:
        arq.write("escreve uma única string\nque pode ter barras n\n")


def escrever_com_writelines():
    """Grava uma lista de strings usando writelines()."""
    lista = ["nome1\n", "nome2\n", "nome3\n", "homer\n"]
    with ARQUIVO.open("w", encoding="utf-8") as arq:
        arq.writelines(lista)


def append_exemplo():
    """Adiciona texto no final do arquivo (append)."""
    with ARQUIVO.open("a", encoding="utf-8") as arq:
        arq.write("adicionando linha no final do arquivo\n")


def ler_modo_texto():
    """Lê o arquivo em modo texto e mostra diferentes formas de leitura."""
    with ARQUIVO.open("r", encoding="utf-8") as arq:
        conteudo = arq.read()
    print("\nConteúdo lido com read():\n", conteudo)

    with ARQUIVO.open("r", encoding="utf-8") as arq:
        arq.seek(0)
        primeira = arq.readline()
        print("Primeira linha ->", primeira.strip())

    with ARQUIVO.open("r", encoding="utf-8") as arq:
        linhas = arq.readlines()
        print("\nLinhas (lista):", linhas)


def ler_modo_binario():
    """Lê o arquivo em modo binário e decodifica para string."""
    with ARQUIVO.open("rb") as arq:
        dados = arq.read()
    print("\nTipo lido em binário:", type(dados))
    try:
        texto = dados.decode("utf-8")
        print("Conteúdo decodificado:\n", texto)
    except Exception as e:
        print("Não foi possível decodificar:", e)


def iterar_arquivo():
    """Mostra como iterar sobre o arquivo linha a linha (gerador)."""
    with ARQUIVO.open("r", encoding="utf-8") as arq:
        print("\nIterando sobre o arquivo:")
        for i, linha in enumerate(arq, start=1):
            print(f"{i}: {linha.strip()}")


def main():
    # garante arquivo de exemplo
    criar_arquivo_exemplo()

    # exemplos de escrita
    escrever_simples()
    escrever_com_writelines()
    append_exemplo()

    # leitura em texto e binário
    ler_modo_texto()
    ler_modo_binario()
    iterar_arquivo()


if __name__ == "__main__":
    main()

