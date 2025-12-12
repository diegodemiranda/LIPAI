""" Ex02 - Solicite ao usuário, uma única vez, as notas no formato n1; n2; n3; ...
Apresente:
 - a média aritmética das notas;
 - a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou
   reprovado (média < 4.0).
"""

from typing import List


def parse_notas(entrada: str) -> List[float]:
    """Converte a string de entrada em lista de floats.

    Espera notas separadas por ';'. Ignora itens vazios.
    Aceita vírgula como separador decimal (ex: 7,5).
    Lança ValueError se algum item não puder ser convertido.
    """
    partes = [p.strip() for p in entrada.split(";") if p.strip()]
    if not partes:
        raise ValueError("Nenhuma nota informada")
    notas = []
    for p in partes:
        # permite 7,5 ou 7.5
        p_norm = p.replace(",", ".")
        notas.append(float(p_norm))
    return notas


def situacao_por_media(media: float) -> str:
    if media > 6.0:
        return "Aprovado"
    if 4.0 <= media <= 6.0:
        return "Recuperação"
    return "Reprovado"


def main() -> None:
    entrada = input("Entre todas as notas separadas por ';' -> ")
    try:
        notas = parse_notas(entrada)
    except ValueError as exc:
        print(f'Erro na entrada: {exc}')
        return

    media = sum(notas) / len(notas)
    print(f'Média das notas -> {media:.2f}')
    print(situacao_por_media(media))


if __name__ == "__main__":
    main()
