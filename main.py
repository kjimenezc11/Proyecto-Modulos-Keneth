# Proyecto: [Modulos PY]
# Estudiante: [Keneth Jimenez Castro]
# Fecha de Inicio: [22/08/2025]
# Fecha de Entrega: [12/09/2025]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
from analisis_datos import *


def saludar():
    print('Hola desde la funcion')

if __name__ == '__main__':
    compras = generar_lista_compras()
    print(compras)
    media = media(list(compras.values()))
    print('Promedio de costo por articulo :', media)

    mediana = mediana(list(compras.values()))
    print(f'Mediana de costo por articulo :', mediana)