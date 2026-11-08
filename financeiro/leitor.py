from abc import ABC, abstractmethod

import csv, json
from datetime import date

from financeiro.lancamento import Lancamento
from financeiro.categoria import Categoria


#* Classe Abstrata
class Leitor(ABC):
    @abstractmethod
    def ler(self, caminho: str) -> list[Lancamento]:
        ...


#* Classe Concreta
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


#*  Classe Concreta
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