import csv
from datetime import date

from financeiro.leitor import Leitor
from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria

class LeitorCSV(Leitor):
    def ler(self, caminho: str) -> list[Lancamento]:
        lancamentos = []

        with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                categoria = Categoria(linha["categoria"])

                lancamento = Lancamento(
                    linha["descricao"],
                    float(linha["valor"]),
                    date.fromisoformat(linha["data"]),
                    categoria
                )

                lancamentos.append(lancamento)

        return lancamentos
