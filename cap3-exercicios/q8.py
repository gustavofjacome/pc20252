inicio, fim = map(int, input("Digite o horario de inicio e fim: 10").split())
duracao = fim - inicio
horas = duracao // 60
minutos = duracao % 60


print(horas,":",minutos,sep="")