def agregar_gasto(lista_gastos):
    l=len(lista_gastos)
    print("--------------------------Agregar Gastos------------------------------")
    descripcion=input('Ingrese la descripcion del nuevo gasto: ')
    categoria=input('Ingrese la categoria a la cual pertences el nuevo gasto: ')
    monto=float(input('Ingrese el monto del nuevo gasto: '))
    lista_gastos.append([l+1,descripcion,categoria,monto])
    print('-----------------------------------------------------------------')
    print('1. Agregar otro gasto\n2. Ir a menu')
    opcion=int(input('Ingrese la opcion que desea: '))
    if opcion==1:
        agregar_gasto(lista_gastos)
    return lista_gastos
    