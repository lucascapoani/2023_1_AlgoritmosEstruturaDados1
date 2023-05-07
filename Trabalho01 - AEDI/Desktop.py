from Computador import Computador

#  A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte.
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    #  Esta classe reimplementa o método getInformacoes() herdado de computador.
    def getInformacoesDesktop(self):
        super().getInformacoes()
        return f"Potência da Fonte: {self._potenciaDaFonte}"

    # Implementação do método cadastrar para Desktop
    def cadastrar(self):
        print("Cadastrando desktop...")