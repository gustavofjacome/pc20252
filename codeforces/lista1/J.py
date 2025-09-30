valor = int(input())

valor100 = valor // 100
valor50 = valor % 100 // 50
valor20 = valor % 100 % 50 // 20
valor10 = valor % 100 % 50 % 20 // 10  
valor5 = valor % 100 % 50 % 20 % 10 // 5
valor2 = valor % 100 % 50 % 20 % 10 % 5 // 2
valor1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1


print(f'{valor}\n'
      f'{valor100} nota(s) de R$ 100,00\n'
      f'{valor50} nota(s) de R$ 50,00\n'
      f'{valor20} nota(s) de R$ 20,00\n'
      f'{valor10} nota(s) de R$ 10,00\n'
      f'{valor5} nota(s) de R$ 5,00\n'
      f'{valor2} nota(s) de R$ 2,00\n'
      f'{valor1} nota(s) de R$ 1,00')
