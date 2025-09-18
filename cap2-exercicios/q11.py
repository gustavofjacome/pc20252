x = int(input("Digite o codigo de 4 digitos: "))


milhar = x // 1000           # 1
centena = (x // 100) % 10    # 2
dezena = (x // 10) % 10      # 3
unidade = x % 10             # 4


x_invertido = unidade*1000 + dezena*100 + centena*10 + milhar

print(x_invertido)  # 4321




#fonte: https://www.quora.com/Is-there-any-way-to-reverse-the-digits-of-an-integer-mathematically
