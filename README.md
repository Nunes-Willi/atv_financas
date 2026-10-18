# 💰 Sistema Financeiro em Python

<sub>Projeto acadêmico da disciplina POO-II.</sub>

Projeto acadêmico desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)** e **Pytest**. O sistema permite registrar receitas e despesas, calcular saldos, realizar fechamentos financeiros, conciliar lançamentos e gerar extratos mensais.

O projeto também utiliza o padrão **Strategy** para permitir diferentes regras de cálculo de rendimento, juros e correção monetária, facilitando a extensão do sistema sem precisar modificar as classes existentes.

## Funcionalidades

- Criar e validar contas.
- Registrar receitas e despesas.
- Categorizar lançamentos.
- Calcular saldo automaticamente.
- Aplicar estratégias de rendimento ao saldo.
- Calcular juros simples e compostos.
- Aplicar correção monetária por taxa.
- Realizar fechamento financeiro.
- Conciliar lançamentos do sistema e do banco.
- Gerar extrato por mês/ano.
- Executar testes unitários com Pytest.

## Estrutura do projeto

```text
atv_financas/
├── financeiro/
│   ├── __init__.py
│   ├── categoria.py
│   ├── lancamento.py
│   ├── conta.py
│   ├── fechamento.py
│   ├── conciliacao.py
│   ├── extrato.py
│   ├── estrategia_rendimento.py
│   ├── estrategia_juros.py
│   └── estrategia_correcao.py
│
├── tests/
│   ├── test_categoria.py
│   ├── test_lancamento.py
│   ├── test_conta.py
│   ├── test_fechamento.py
│   ├── test_conciliacao.py
│   ├── test_extrato.py
│   ├── test_estrategia_rendimento.py
│   ├── test_estrategia_juros.py
│   └── test_estrategia_correcao.py
│
├── requirements.txt
└── README.md
```

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/Nunes-Willi/atv_financas.git
cd atv_financas
```

### 2. Criar e ativar o ambiente virtual

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso o Pytest ainda não esteja instalado no ambiente:

```bash
pip install pytest
```

### 4. Executar os testes

```bash
pytest
```

## Arquitetura

| Classe | Responsabilidade |
|---|---|
| `Conta` | Gerencia os lançamentos e calcula o saldo, podendo aplicar uma estratégia de rendimento. |
| `Categoria` | Classifica receitas e despesas. |
| `Lancamento` | Representa uma movimentação financeira, com descrição, valor, data e categoria. |
| `Fechamento` | Consolida receitas, despesas e saldo de um conjunto de lançamentos. |
| `Conciliacao` | Compara lançamentos do sistema com lançamentos bancários. |
| `Extrato` | Gera um resumo dos fechamentos de determinado período. |
| `EstrategiaRendimento` | Define a interface para os cálculos de rendimento. |
| `EstrategiaJuros` | Define a interface para os cálculos de juros. |
| `EstrategiaCorrecao` | Define a interface para os cálculos de correção monetária. |

## Decisões de projeto

**Fechamento:** utiliza uma referência para a lista de lançamentos, evitando duplicação de dados e mantendo a consistência com os lançamentos fornecidos à classe.

**Conciliação:** foi implementada como uma classe própria, pois sua função é comparar dois conjuntos de lançamentos, diferente do fechamento, que consolida um único conjunto.

**Estratégias separadas:** as estratégias de rendimento, juros e correção monetária possuem interfaces independentes: `EstrategiaRendimento`, `EstrategiaJuros` e `EstrategiaCorrecao`. Essa escolha foi feita porque cada conceito possui uma finalidade e uma forma de cálculo diferente. O rendimento pode acrescentar um percentual ao saldo, os juros podem ser simples ou compostos, e a correção monetária atualiza um valor conforme uma taxa. Dessa forma, cada interface possui suas próprias implementações, facilitando a manutenção e evitando misturar responsabilidades distintas.

**Escolha e armazenamento da estratégia:** na classe `Conta`, a estratégia de rendimento é passada como parâmetro para o método `calcular_saldo()`, em vez de ser armazenada como atributo da conta. Essa decisão permite escolher a regra no momento do cálculo, sem manter uma estratégia fixa durante toda a existência da conta. Assim, a mesma conta pode calcular o saldo sem rendimento ou aplicar um percentual, dependendo da estratégia recebida. As estratégias de juros e correção monetária também possuem interfaces próprias, mas ainda não estão integradas a uma operação específica da conta ou do fechamento.

**Extensibilidade:** o padrão Strategy permite adicionar novas regras de cálculo sem modificar as classes existentes que utilizam a interface correspondente. Por exemplo, podemos criar uma classe `RendimentoMensal` que implemente `EstrategiaRendimento` e defina uma nova regra de rendimento. Depois de implementada, essa estratégia poderá ser utilizada por `Conta` por meio do método `calcular_saldo()`, sem necessidade de alterar o código interno desse método. O mesmo princípio permite criar novas estratégias de juros ou correção monetária, desde que implementem suas respectivas interfaces.

**Casos especiais:**

- Sem lançamentos no período: o extrato deve apresentar totais iguais a zero, conforme a implementação da classe.
- Diferença na conciliação: o sistema informa a divergência encontrada entre os conjuntos de lançamentos.
- Sem rendimento: a estratégia retorna o saldo calculado sem acréscimos.
- Taxa de rendimento igual a zero: o valor permanece inalterado.
- Percentual de rendimento inválido: `PercentualRendido` rejeita percentuais inferiores a 0 ou superiores a 100.


## Testes

Os testes unitários utilizam **Pytest** para verificar o comportamento das classes e das estratégias.

Entre os cenários testados estão:

- Criação e validação de contas.
- Adição e remoção de lançamentos.
- Cálculo do saldo com receitas e despesas.
- Cálculo do saldo sem rendimento e com rendimento percentual.
- Cálculo de juros simples e compostos.
- Aplicação e ausência de correção monetária.
- Validação de percentuais de rendimento.
- Comportamentos com capital, taxa ou valores iguais a zero.

Os testes ajudam a identificar erros e verificar se novas implementações continuam respeitando os comportamentos esperados.

## Autor

**William Roberto Nunes**

Bacharelado em Sistemas de Informação