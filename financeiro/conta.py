from financeiro.lancamento import Lancamento
from financeiro.estrategia_rendimento import EstrategiaRendimento

class Conta:
    def __init__(self, nome: str, idade: int, saldo: float) -> None:
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.lancamentos = []
        
    def abrir_conta(self) -> bool:
        if self.nome == "":
            raise ValueError("Precisa de nome do Usuário da conta")
        elif 110 <= self.idade <= 18:
            raise ValueError("Precisa ter idade entre 18 e 110 anos")
        
        print(f"Seja Bem Vindo {self.nome}! Estamos contando com seu dinheiro:)")
        return True
    
    def adicionar_lancamento(self, lancamento: Lancamento) -> None:
        self.lancamentos.append(lancamento)
        
    def remover_lancamento(self, lancamento: Lancamento) -> None:
        if lancamento in self.lancamentos:
            self.lancamentos.remove(lancamento)
            
            # Revisar
    def calcular_saldo(self, estrategia_rendimento: EstrategiaRendimento) -> float:
        saldo_atual = self.saldo

        for lancamento in self.lancamentos:
            saldo_atual += lancamento.valor

        return saldo_atual

    def listar_extrato(self) -> None:
        print("=== EXTRATO ===")

        for lancamento in self.lancamentos:
            print(
                f"{lancamento.data} | "
                f"{lancamento.descricao} | "
                f"R$ {lancamento.valor:.2f} | "
                f"{lancamento.categoria.nome}"
            )

        print(f"\nSaldo atual: R$ {self.calcular_saldo():.2f}")
        
    def obter_lancamentos(self) -> list[Lancamento]:
        return self.lancamentos