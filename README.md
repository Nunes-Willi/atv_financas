# 💰 Sistema Financeiro em Python

Projeto acadêmico desenvolvido em **Python** utilizando **Programação Orientada a Objetos** e **Pytest**. O sistema permite registrar receitas e despesas, calcular saldos, realizar fechamentos financeiros, conciliar lançamentos e gerar extratos mensais.

## Funcionalidades

- Criar e validar contas
- Registrar receitas e despesas
- Categorizar lançamentos
- Calcular saldo automaticamente
- Realizar fechamento financeiro
- Conciliar lançamentos do sistema e do banco
- Gerar extrato por mês/ano
- Executar testes unitários com Pytest

## Estrutura do projeto

```text
financeiro/
├── categoria.py
├── lancamento.py
├── conta.py
├── fechamento.py
├── conciliacao.py
└── extrato.py

tests/
├── test_categoria.py
├── test_lancamento.py
├── test_conta.py
├── test_fechamento.py
├── test_conciliacao.py
└── test_extrato.py
```

## Como executar

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd sistema-financeiro
```

### 2. Criar e ativar o ambiente virtual

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
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

### 4. Executar os testes

```bash
pytest
```

## Arquitetura

| Classe | Responsabilidade |
|---------|------------------|
| Conta | Gerencia lançamentos e saldo |
| Categoria | Classifica receitas e despesas |
| Lancamento | Representa uma movimentação financeira |
| Fechamento | Consolida lançamentos de um período |
| Conciliacao | Compara lançamentos do sistema e do banco |
| Extrato | Gera resumo mensal dos fechamentos |

## Decisões de projeto

**Fechamento:** utiliza uma **referência** para a lista de lançamentos, evitando duplicação de dados e mantendo consistência com a conta.

**Conciliação:** foi implementada como uma **classe própria**, pois sua função é comparar dois conjuntos de lançamentos, diferente do fechamento que apenas consolida um único conjunto.

**Casos especiais:**
- Sem lançamentos no período: o extrato retorna totais iguais a zero.
- Diferença na conciliação: o sistema lança uma mensagem de erro informando os totais e a diferença encontrada.