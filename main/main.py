from epidemio_models import Doenca

c = int(input('Contado médio entre os indivíduos: '))
p = float(input('Probabilidade de contaminção: '))
beta = c * p
tempo_de_contaminacao = int(input('Tempo de contaminação: '))
# tempo médio em que um indivíduo pode infectar outras pessoas.
# Para a gripe, o período infecioso é tipicamente de 1 a 3 dias
gama = 1 / tempo_de_contaminacao  # coeficiente de recuperação.

mortalidade = float(input('Mortalidade da doença: '))

corona = Doenca(populacao=900000, beta=beta, gama=gama,
                tDeath=mortalidade, infectado=5100, simulationTime=360, leitos=5623)

corona.run()
corona.plot(mortalidade, c, p)


