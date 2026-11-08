from financeiro.importador_banco import CriadorImportador


class ServicoImportacao:

    def __init__(self, criador_importador):
        self.criador_importador = criador_importador

    def importar(self, banco, caminho):
        importador = self.criador_importador.criar(banco)

        return importador.importar(caminho)


def montar_aplicacao():

    criador_importador = CriadorImportador()

    servico = ServicoImportacao(
        criador_importador
    )

    return servico