B = int(input())
T = int(input())

#valor constante
comprimento = 160 
altura = 70

area_total = comprimento * altura
	
    
area_felix = ((B + T) * altura) // 2
area_marzia = area_total - area_felix
metade = area_total // 2

if area_felix > metade:
	print(1)
	
elif area_marzia > metade:
	print(2)
	
else:
	print(0)