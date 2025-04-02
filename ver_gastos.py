from tabulate import tabulate
def ver_gastos(lista_gastos):
    tamano=len(lista_gastos)
    print('-------------------------------Lista de gastos-------------------------------------')
    print(f"id      Titulo                        Descripcion                           Estado")
    for i in range(tamano):
        id=lista_gastos[i][0]
        descripcion=lista_gastos[i][1]
        categoria=lista_gastos[i][2]
        monto=lista_gastos[i][3]
        print(f"{id}     {descripcion}        {categoria}      {monto}")
    print(tabulate(lista_gastos,headers=['Id','Titulo','Descripcion','Estado'],tablefmt="grid"))