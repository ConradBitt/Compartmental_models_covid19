from epidemio_models import Doenca

c = int(input('Contado médio entre os indivíduos: '))
p = float(input('Probabilidade de contaminção: '))
beta = c * p
tempo_de_contaminacao = int(input('Tempo de contaminação: '))
gama = 1 / tempo_de_contaminacao

mortalidade = float(input('Mortalidade da doença: '))

populacao = int(input('População: '))
infectado = int(input('Infectados: '))
tempo_simulacao = int(input('Tempo em dias decorrido desde o primeiro caso: '))

corona = Doenca(populacao=populacao, beta=beta, gama=gama,
                tDeath=mortalidade, infectado=infectado, simulationTime=tempo_simulacao, leitos=5623)

corona.run()
corona.plot(mortalidade, c, p)


