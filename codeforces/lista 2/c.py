nome = input()
salario = float(input())
vendas = float(input())


salarioTotal = salario + (vendas*15/100)

print(f'{nome}\n'
      f'R$ {salarioTotal:.2f}')
