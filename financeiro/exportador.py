from abc import ABC, abstractmethod

#*  Classe abstrata
class ExportarRelatorio(ABC):
    def exportar(self, relatorio):
        documento = self.criar_doc(relatorio)
        
        self.add_cabecalho(documento, relatorio)
        self.add_corpo(documento, relatorio)
        self.add_rodape(documento, relatorio)
        
        self.salvar(documento)
        
    @abstractmethod
    def criar_doc(self, relatorio):
        pass
    

#* Classe concreta - CSV
class ExportarCSV(ExportarRelatorio):
    def criar_doc(self, relatorio):
        return []
    
    def add_cabecalho(self, documento, relatorio):
       documento.append(["Data", "Descrição", "Valor"])
       
    def add_corpo(self, documento, relatorio):
        for lancamento in relatorio:
            documento.append([
                lancamento.data,
                lancamento.descricao,
                lancamento.valor
            ])
            
    def add_rodape(self, documento, relatorio):
        pass
    
    def salvar(self, documento):
        ...
        
#* Classe concreta - HTML
class ExportarHTML(ExportarRelatorio):
    
    def criar_doc(self, relatorio):
        return []
    
    def add_cabecalho(self, documento, relatorio):
        documento.append("<html>")
        documento.append("<body>")
        documento.append("<h1> Extrato </h1>")
        
    def add_corpo(self, documento, relatorio):
        documento.append("<table>")
        
        for lancamento in relatorio:
            documento.append(
                f"<tr>"
                f"<td> {lancamento.data} </td>" 
                f"<td> {lancamento.descricao} </td>"
                f"<td> {lancamento.valor} </td>"
                f"</tr>"
            )
            
        documento.append("</table>")
            
    def add_rodape(self,documento, relatorio):
        documento.append("</body>")
        documento.append("</html>")
        
        
    def salvar(self, documento):
        ...

#* Classe concreta - PDF
class ExportarPDF(ExportarRelatorio):

    def criar_doc(self, relatorio):
        return []

    def add_cabecalho(self, documento, relatorio):
        documento.append("RELATÓRIO FINANCEIRO")
        documento.append("Data | Descrição | Valor")

    def add_corpo(self, documento, relatorio):
        for lancamento in relatorio:
            documento.append(
                f"{lancamento.data} | "
                f"{lancamento.descricao} | "
                f"{lancamento.valor}"
            )

    def add_rodape(self, documento, relatorio):
        documento.append("FIM DO RELATÓRIO")

    def salvar(self, documento):
        pass
