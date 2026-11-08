from financeiro.servico_importacao import ServicoImportacao

class ImportadorFake:

    def importar(self, caminho):
        return ["Lançamento de teste"]


class CriadorImportadorFake:

    def criar(self, banco):
        return ImportadorFake()


class TestServicoImportacao:

    def test_importar(self):
        criador = CriadorImportadorFake()

        servico = ServicoImportacao(criador)

        resultado = servico.importar(
            "BANCO_X",
            "arquivo.csv"
        )

        assert resultado == ["Lançamento de teste"]

    def test_recebe_criador_importador(self):
        criador = CriadorImportadorFake()

        servico = ServicoImportacao(criador)

        assert servico.criador_importador is criador