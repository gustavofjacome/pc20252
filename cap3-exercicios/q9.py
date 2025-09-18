dias = int(input("\nDigite a quantidade de dias desde o início do ano: "))

semanas = dias // 7
dias_restantes = dias % 7


print(semanas, "semana(s)", dias_restantes, "dia(s)")
