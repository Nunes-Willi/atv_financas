from financeiro.exportador_relatorio import ExportRelatorio

class ExportadorHTML(ExportRelatorio):
    
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