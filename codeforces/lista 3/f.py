codigo, quantidade = map(int, input().split())


#definindo as constantes
cachorroQuente = 4.00
x_salada = 4.50
x_bacon = 5.00
torradaSimples = 2.00
Refrigerante = 1.50



if (codigo == 1):
    total = cachorroQuente*quantidade
    print(f'Total: R$ {total:.2f}')

if (codigo == 2):
    total = x_salada*quantidade
    print(f'Total: R$ {total:.2f}')   

if (codigo == 3):
    total = x_bacon*quantidade
    print(f'Total: R$ {total:.2f}')

if (codigo == 4):
    total = torradaSimples*quantidade
    print(f'Total: R$ {total:.2f}')    

if (codigo == 5):
    total = Refrigerante*quantidade
    print(f'Total: R$ {total:.2f}')    