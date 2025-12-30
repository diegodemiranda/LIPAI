"""
Exercício 03 - Implementar uma classe Participacao
Arquivo reformulado e formatado corretamente.
"""
# Tentativa segura de importar Aluno e Projeto; se não existirem, criamos
# substitutos mínimos para que os testes locais funcionem sem dependências.
try:
    from ex01 import Aluno
except Exception:
    class Aluno:
        @classmethod
        def criar_de_string(cls, s: str):
            # Retorna a string "desempacotada" como representação simplificada
            return str(s).strip()

try:
    from ex02 import Projeto
except Exception:
    class Projeto:
        @classmethod
        def criar_projeto(cls, s: str):
            return str(s).strip()


class Participacao:
    """Classe Participacao formatada e funcional.

    Atributos principais:
    - codigo: identificador (int quando possível)
    - data_inicio: string
    - data_fim: string
    - aluno: objeto Aluno (ou representação fallback)
    - projeto: objeto Projeto (ou representação fallback)
    """

    def __init__(self, codigo, data_inicio=None, data_fim=None, aluno=None, projeto=None):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @classmethod
    def criar_participacao(cls, string_participacoes: str):
        """Cria um objeto Participacao a partir de uma string com 5 partes
        separadas por ';' no formato:
          codigo ; "data_inicio" ; "data_fim" ; "aluno_data" ; "projeto_data"

        Faz parsing simples e limpa aspas externas.
        """
        if not string_participacoes or not isinstance(string_participacoes, str):
            raise ValueError("Erro -> a string deve ser válida")

        # separa por ';' e faz strip nas partes
        partes = [p.strip() for p in string_participacoes.split(';')]
        if len(partes) != 5:
            raise ValueError("String deve ter 5 partes separadas por ';'. Encontrado: {}".format(len(partes)))

        def unquote(s: str) -> str:
            s = s.strip()
            if (len(s) >= 2) and ((s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'")):
                return s[1:-1].strip()
            return s

        codigo_str = unquote(partes[0])
        data_inicio = unquote(partes[1])
        data_fim = unquote(partes[2])
        aluno_str = unquote(partes[3])
        projeto_str = unquote(partes[4])

        # Tenta converter código para inteiro quando possível
        try:
            codigo = int(codigo_str)
        except Exception:
            codigo = codigo_str

        # Cria objetos Aluno e Projeto usando as fábricas se existirem
        try:
            aluno_obj = Aluno.criar_de_string(aluno_str)
        except Exception:
            aluno_obj = aluno_str

        try:
            projeto_obj = Projeto.criar_projeto(projeto_str)
        except Exception:
            projeto_obj = projeto_str

        return cls(codigo, data_inicio, data_fim, aluno_obj, projeto_obj)

    def __str__(self):
        return (
            f"Participacao [codigo={self.codigo}, data_inicio={self.data_inicio},"
            f" data_fim={self.data_fim},\n  aluno={self.aluno},\n  projeto={self.projeto}]"
        )


# Bloco de testes (executa somente ao rodar diretamente)
if __name__ == "__main__":
    print('\n----- Início do Teste Classe Participacao ----\n')

    DATA = '1234 ; "01-10-2025" ; "29-12-2026" ; "SP001, José da Silva, jose@email.com" ; "2, Laboratório de IA, Maria Silva"'

    try:
        participacao = Participacao.criar_participacao(DATA)
        print('Participacao criada com sucesso:')
        print(participacao)
    except Exception as e:
        print('Erro ao criar participacao:', e)

    # --- TESTE 02: SIMULAÇÃO DE ERRO ---
    print('\n--- Iniciando Teste 02 (Deve retornar erro) ---\n')
    DATA_ERRO = '9999;"01-01-2024";"30-06-2024";"SP002, Aluno Sem Email";"3, Projeto X, Prof. Girafales"'

    try:
        participacao_erro = Participacao.criar_participacao(DATA_ERRO)
        print('Participacao (erro) criada (não esperado):')
        print(participacao_erro)
    except ValueError as e:
        print('Mensagem de erro capturada:', e)
    except Exception as e:
        print('Erro inesperado capturado:', e)
