from Fisica import Fisica
from Cidade import Cidade
from Juridica import Juridica

c1 = Cidade("POA")
c2 = Cidade("Capão da Canoa")

pf1 = Fisica("João", "33423349", c1, "000.000.000-11")
pj1 = Juridica("Mercado do Zé", "33669585", c2, "00.111.2222/0001-02")
pf2 = Fisica("Maria", "99559995", c2, "331.111.000-11")

#pf.imprimir()
pj1.imprimir()

pj1.addFuncionario(pf1)
pj1.addFuncionario(pf2)

pj1.imprimir()
