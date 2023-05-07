# Uma classe abstrata chamada de Computador que contém os atributos/propriedades: modelo, cor e preço.
from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo = None, cor = None, preco = 0):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    # Esta classe possui um método getInformacoes() que retorna todos os valores dos atributos.
    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: R${self.preco}"

    # Esta classe também possui um método abstrato cadastrar().
    @abstractmethod
    def cadastrar(self):
        print("Cadastrando produto...")