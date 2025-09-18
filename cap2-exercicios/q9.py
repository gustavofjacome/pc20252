'''
No interpretador Python3 crie uma variável `x` com um valor inteiro e, logo a seguir, uma variável `digito` que contém o **último dígito (dígito das unidades)** da variável `x`.  
Exemplo: Se `x = 73623`, então `digito = 3`.

Use operações matemáticas para determinar o último dígito de um número inteiro:
'''

x = int(input())

digito = x%10

print(digito)