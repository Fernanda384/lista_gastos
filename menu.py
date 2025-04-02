from agregar_gasto import agregar_gasto
from eliminar_gasto import eliminar_gasto
from ver_gastos import ver_gastos
def menu(lista_gastos):
    print('----------------------------Bienvenido---------------------------')
    print('\n1. Agregar nuevo gasto\n2. Eliminar gasto\n3. Ver resumen categoria\n4. Calcular total gastos\n0. Salir')
    opcion=int(input('Seleccione la opcion que desea: '))
    if opcion==1:
        lista_gastos=agregar_gasto(lista_gastos)
        menu(lista_gastos)
    elif opcion==2:
        lista_gastos=eliminar_gasto(lista_gastos)
        menu(lista_gastos)
    elif opcion==3:
        ver_gastos(lista_gastos)
        menu(lista_gastos)
    else:
        menu(lista_gastos)
def inicio():
    lista_gastos=[]
    menu(lista_gastos)
inicio()