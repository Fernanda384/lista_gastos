def ver_resumen_categoria(lista_gastos):
    lista_categorias=[]
    categoria=lista_gastos[0][2]
    lista_gastos.append(categoria)
    for i in range(1,len(lista_gastos)):
        categoria=lista_gastos[i][2]
        if categoria.upper() in lista_categorias:
            continue
        else:
            lista_categorias.append(categoria)
    