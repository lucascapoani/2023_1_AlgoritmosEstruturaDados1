from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook

m1 = Desktop("iMac 24", "Prata", 15000, 500)
print(m1.getInformacoes())
print(m1.getInformacoesDesktop())
print(" OU ")
print(m1.modelo," - ",m1.cor," - ",m1.preco," - ",m1._potenciaDaFonte)
m1.cadastrar()

print(" ----------------------------- ")

m2 = Notebook("Dell Inspiron", "Preto", 3500, 8)
print(m2.getInformacoes())
print(m2.getInformacoesNotebook())
print(" OU ")
print(m2.modelo," - ",m2.cor," - ",m2.preco," - ",m2.getInformacoesNotebook())
m2.cadastrar()