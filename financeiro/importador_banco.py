from financeiro.leitor import LeitorCSV, LeitorJSON

class ImportadorBancoX:
    def __init__(self):
        self.leitor = LeitorCSV()
    
    def importar(self, caminho):
        return self.leitor.ler(caminho)
    
class ImportadorBancoY:
    def __init__(self):
        self.leitor = LeitorJSON()
        
    def importar(self, caminho):
        return self.leitor.ler(caminho)
    
class CriadorImportador:

    def criar(self, banco):
        if banco == "BANCO_X":
            return ImportadorBancoX()

        if banco == "BANCO_Y":
            return ImportadorBancoY()

        raise ValueError("Banco desconhecido")