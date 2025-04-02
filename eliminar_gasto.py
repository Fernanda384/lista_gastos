from ver_gastos import ver_gastos
def eliminar_gasto(lista_gasto):
    l=len(lista_gasto)
    ver_gastos(lista_gasto)
    print('---------------------Eliminar gasto--------------------------')
    lista_borrar=int(input('Ingresa el id del gasto que desea borrar '))-1
    #Agregar estar seguro de borrar esta lista
    if lista_borrar<l  and lista_borrar>-1:
        lista_gasto.pop(lista_borrar)
        for i in range(l):
            lista_gasto[i][0]=i+1
    else:
        print('Ingrese un valor valido')
        eliminar_gasto(lista_gasto)
    return lista_gasto