class Conta:
    def __init__(self, nome: str, idade: int, saldo: float) -> None:
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        
    def abrir_conta(self) -> bool:
        if self.nome == "":
            raise ValueError("Precisa de nome do Usuário da conta")
        elif self.idade < 18:
            raise ValueError("Precisa ser maior de idade para abrir conta")
        elif self.saldo <= 0:
            raise ValueError ("É preciso ter um SALDO maior que 0(zero)!!")
        
        print(f"Seja Bem Vindo {self.nome}! Estamos contando com seu dinheiro:)")
        return True