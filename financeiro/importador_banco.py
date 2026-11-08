from financeiro.leitor import LeitorCSV, LeitorJSON

class ImportadorBancoX:
    def __init__(self, leitor):
        self.leitor = leitor
    
    def importar(self, caminho):
        return self.leitor.ler(caminho)
    
class ImportadorBancoY:
    def __init__(self, leitor):
        self.leitor = leitor
        
    def importar(self, caminho):
        return self.leitor.ler(caminho)
    
class CriadorImportador:

    def criar(self, banco):
        if banco == "BANCO_X":
            return ImportadorBancoX(LeitorCSV())

        if banco == "BANCO_Y":
            return ImportadorBancoY(LeitorJSON())

        raise ValueError("Banco desconhecido")