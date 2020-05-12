from epidemio_models import Doenca
# Levando em conta os dados da COVID-19

c = 3  # contato entre as pessoas
p = 0.10  # probabilidade de contaminar
beta = c * p
tempo_de_contaminacao = 4  # o tempo de residência no compartimento infeccioso, isto é, o
# tempo médio em que um indivíduo pode infectar outras pessoas.
# Para a gripe, o período infecioso é tipicamente de 1 a 3 dias
gama = 1 / tempo_de_contaminacao  # coeficiente de recuperação.

mortalidade = 0.04

corona = Doenca(populacao=900000, beta=beta, gama=gama,
                tDeath=mortalidade, infectado=5100, simulationTime=360, leitos=5623)

corona.run()
corona.plot(mortalidade, c, p)


