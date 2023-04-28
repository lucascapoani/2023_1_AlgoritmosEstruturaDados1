from Computador import Computador

#A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria.
class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    # Esta classe reimplementa o método getInformacoes() herdado de computador.
    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        print("Cadastrando notebook...")
        # Implementação do método cadastrar para Notebook
