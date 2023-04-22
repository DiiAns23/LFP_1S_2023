# Torres de HANOI
def hanoi(discos, origen, auxiliar, destino):
    if discos==1:
        print("Mover de", origen, "a", destino)
    else:
        hanoi(discos-1, origen, destino, auxiliar)
        print("Mover de", origen, "a", destino)
        hanoi(discos-1, auxiliar, origen, destino)
hanoi(9,1,2,3)


# Funcion Ackerman
def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m>0 and n==0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))


print(ackerman(3, 7))