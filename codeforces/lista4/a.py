alcool, gasolina, dist_alcool, dist_gasolina = map(float, input().split())


rendimentoAlcool = alcool / dist_alcool
rendimentoGasolina = gasolina / dist_gasolina

if (rendimentoAlcool < rendimentoGasolina):
    print('A')

if (rendimentoGasolina < rendimentoAlcool):
    print('G')

if (rendimentoGasolina == rendimentoAlcool):
    print('G')