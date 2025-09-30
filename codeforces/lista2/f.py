distancia = int(input())  # km
velocidade = int(input())  # km/h

tempo = distancia / velocidade  
horas = int(tempo)              
minutos = int((tempo - horas) * 60)  

print(f'{horas:02d}:{minutos:02d}')
