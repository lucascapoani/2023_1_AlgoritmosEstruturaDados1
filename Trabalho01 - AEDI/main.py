from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

m1 = Desktop("iMac 24", "Prata", 15000, 500)
print(m1.getInformacoes())
m1.cadastrar()

m2 = Notebook("Dell Inspiron", "Preto", 3500, 8)
print(m2.getInformacoes())
m2.cadastrar()