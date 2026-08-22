from financeiro.lancamento import Lancamento
class Conta:
    def __init__(self, nome: str, idade: int, saldo: float) -> None:
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.lancamentos = []
        
    def abrir_conta(self) -> bool:
        if self.nome == "":
            raise ValueError("Precisa de nome do Usuário da conta")
        elif self.idade < 18:
            raise ValueError("Precisa ser maior de idade para abrir conta")
        # elif self.saldo <= 0:
        #     raise ValueError ("É preciso ter um SALDO maior que 0(zero)!!")
        
        print(f"Seja Bem Vindo {self.nome}! Estamos contando com seu dinheiro:)")
        return True
    
    def adicionar_lancamento(self, lancamento: Lancamento) -> None:
        self.lancamentos.append(lancamento)
        
    def remover_lancamento(self, lancamento: Lancamento) -> None:
        if lancamento in self.lancamentos:
            self.lancamentos.remove(lancamento)

    def calcular_saldo(self) -> float:
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