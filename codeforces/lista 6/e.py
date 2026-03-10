def dia_da_semana(h, d):
    dias = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]

    diaAtual = dias.index(h)

    indiceEvento = (diaAtual + d) % 7

    return dias[indiceEvento]
