from financeiro.conta import Conta

class TestConta:
    def test_criar_conta(self):
        usuario = Conta("William", 20, 1000.0)
        
        assert usuario.abrir_conta() is True