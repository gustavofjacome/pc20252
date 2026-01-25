def sublista_sem_menor(lista):
    novaSemMenor = lista.copy()       
    novaSemMenor.remove(min(novaSemMenor))
    return novaSemMenor
