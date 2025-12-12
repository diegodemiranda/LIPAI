# Reflexão: Arquitetura e Design de Funções em Python

## 1. Qual função é mais flexível: ex01 (imprime) ou ex02 (retorna)?

A função do **ex02 (que retorna o valor) é significativamente mais flexível**.

**Por quê?**
A função do `ex01` sofre de **acoplamento com a saída padrão** (console). Ela decide o que fazer com o dado (imprimir), o que limita drasticamente sua utilidade. Se você precisar salvar o resultado em um banco de dados, enviá-lo para uma API ou usá-lo em outro cálculo, a função do `ex01` se torna inútil.

Já a função do `ex02` segue o princípio de **separação de responsabilidades**: ela apenas calcula o valor e o "devolve" para o chamador. O chamador decide se quer imprimir, armazenar ou transformar esse dado. Em desenvolvimento profissional, funções de lógica raramente devem usar `print()` diretamente.

---

## 2. Qual abordagem é mais flexível: parâmetros fixos (ex02) ou variáveis (ex03/ex04)?

A abordagem do **ex03/ex04 (número variável de argumentos) é mais flexível**.

**Por quê?**
Funções com parâmetros fixos (`ex02`) definem um **contrato estrito**. Se a regra de negócio mudar e você precisar somar 4 números em uma função que só aceita 3, terá que refatorar o código.

As abordagens de número variável permitem que a mesma função atenda a múltiplos cenários (somar 2, 10 ou 1000 números) sem alteração na sua estrutura interna, aumentando a escalabilidade.

---

## 3. Tuplas (ex03) vs *args (ex04): Quando usar cada uma?

Ambas permitem variabilidade, mas a escolha depende da **origem do dado**:

### Uso de Tupla/Lista (ex03)
* **Situação ideal:** Quando os dados já existem previamente agrupados em uma coleção (ex: uma lista de preços vinda de um Banco de Dados).
* **Justificativa:** Passar a coleção inteira é mais limpo semanticamente e evita ter que "desempacotar" a lista apenas para passá-la para a função.

### Uso de *args (ex04)
* **Situação ideal:** Quando os valores são passados de forma "avulsa" no código ou ao criar funções utilitárias (wrappers).
* **Justificativa:** O `*args` oferece uma sintaxe mais limpa (*syntax sugar*) para quem chama a função, dispensando a necessidade de criar colchetes `[]` ou parênteses `()` extras na hora de escrever o código.