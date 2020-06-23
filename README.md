# Compartmental model covid19
Objetivo: Aplicar o modelo epidemiológico SIR utilizado em epidemias de gripe/ebola/zika para analisar o surto de SARS-Cov2 pelas cidades baseado no número de suscetíveis, infectados e recuperados.

# Modelo SIR 
Vamos modelar a dinâmica de uma doença (gripe, por exemplo), que se propaga numa certa população. Para isso, começamos por dividir a população em 3 grupos:

        * S = {Suscetíveis} - os que podem adquirir o vírus, mas que atualmente não estão infectados;
        * I = {Infectados} - os que estão infectados com o vírus e podem transmiti-lo a outros;
        * R = {Removidos/Recuperados} - os que não podem contrair o vírus, ou porque recuperaram permanentemente
                                    e ficaram imunes (pelo menos durante o período em análise), ou porque
                                    são naturalmente imunes ou porque morreram!

# Equações do modelo
O modelo SIR leva em conta um conjunto de três equações, que representam a taxa de variação dos grupos em função do tempo t: 

        dS = beta * [ [S(t) * I (t)] / N ] * dt;
        dI = { [{beta* S(t) * I(t)} / N] - gama * I(t) } * dt;
        dR = - gama * I(t) * dt:



# Coeficientes do Modelo SIR
* Gama : Coeficiente de recuperação. É uma taxa per-capita e por unidade de tempo. O seu recíproco 1/γ, pode ser identificado como o tempo de residência, o tempo médio em que um indivíduo pode infectar outras pessoas. Para a gripe, o período é de 1 a 3 dias. Se o considerarmos igual a 2 dias (Média entre 1 e 3 dias), por exemplo, isto significa que a taxa de recuperação é γ = 1/2 (indivíduo por dia) e portanto em um dia metade dos infetados recuperam – passam para o grupo de recuperados R

* Beta : Coecifiente de transmissão. Suponhamos que cada indivduo entra em contato em média com C outros, escolhidos aleatoriamente. C diz-se a 'taxa de contato per-capita' por unidade de tempo. Considerando a hipótese de uma população homogeneamente misturada, C é constante. Se p é a probabilidade de que um contato resulte em contágio e, uma vez que existem I(t) indivíduos infetados no total, isso significa que o número de novas infeções, no intervalo de tempo é C \* p = beta. O coenficiente de transmissão depende do contato médio (C) entre indivíduos de uma população e a probabilidade (p) de um infectado infectar um individo saudável.

# Modo de usar

Ao executar o arquivo **main.py**, será perguntado no prompt:
```
[In]
    Contado médio entre os indivíduos: 3  # aqui deve ser um número inteiro
    Probabilidade de contaminção: 0.1  # aqui deve ser a probabilidade normalizada.
    Tempo de contaminação: 4  # Tempo em dias, também um número inteiro.
    Mortalidade da doença: 0.07  # taxa de mortalidade normalizada.
[Out]
```
<p align="left">
    <img src="figure_SIR_model" width=35%>
</p>

**Contributing:** conrad.bittencourt@gmail.com

# Referências:
[1] https://doi.org/10.1137/S0036144500371907

[2] http://doi.org/10.24927/rce2017.020

Dependencies
------------



Installation requires [matplotlib](https://matplotlib.org/).
