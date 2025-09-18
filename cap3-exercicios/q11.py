distancia, velocidade = map(int, input("Digite a distancia entre as cidades e a velocidade do carro: ").split())

tempo_horas = distancia / velocidade

hh = int(tempo_horas)
mm = int((tempo_horas - hh) * 60)


print("Tempo de viagem -> ", hh,":",mm,sep="")