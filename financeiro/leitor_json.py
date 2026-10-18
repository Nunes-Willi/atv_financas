import json
from datetime import date

from financeiro.leitor import Leitor
from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria

class LeitorJSON(Leitor):
    def ler(self, caminho: str) -> list[Lancamento]:
        lancamentos = []

        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        for registro in dados:
            categoria = Categoria(registro["categoria"])

            lancamento = Lancamento(
                registro["descricao"],
                float(registro["valor"]),
                date.fromisoformat(registro["data"]),
                categoria
            )

            lancamentos.append(lancamento)

        return lancamentos