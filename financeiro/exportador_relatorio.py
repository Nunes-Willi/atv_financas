from abc import ABC, abstractmethod

class ExportRelatorio(ABC):
    def exportar (self, relatorio):
        documento = self.criar_doc(relatorio)
        
        self.add_cabecalho = (documento, relatorio)
        self.add_corpo = (documento, relatorio)
        self.add_rodape = (documento, relatorio)
        
        self.salvar(documento)
        
    @abstractmethod
    def criar_doc(self, relatorio):
        pass