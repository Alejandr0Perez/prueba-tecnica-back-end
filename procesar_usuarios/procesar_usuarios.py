import json
import locale
from datetime import datetime, date

# Configurar la localización en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Elimina usuarios duplicados y suma sus saldos
def eliminar_duplicados_y_sumar_saldos(usuarios):
    """
    Combina usuarios con el mismo nombre completo y suma sus saldos.
    """
    usuarios_dict = {}
    for usuario in usuarios:
        nombre = usuario["nombre_completo"]
        if nombre not in usuarios_dict:
            usuarios_dict[nombre] = usuario
        else:
            usuarios_dict[nombre]["saldo"] += usuario["saldo"]
    return list(usuarios_dict.values())

# Separa el nombre completo en partes: nombre, apellido paterno y apellido materno
def separar_nombre(nombre_completo):
    """
    Divide el nombre completo en nombre, apellido paterno y apellido materno.
    """
    nombres = nombre_completo.split()
    nombre = nombres[0]
    apellido_paterno = nombres[1]
    apellido_materno = nombres[2]
    return nombre, apellido_paterno, apellido_materno

# Convierte la fecha de nacimiento a un formato más simple: 'YYYY-MM-DD'
def formatear_fecha(fecha_nacimiento):
    """
    Cambia la fecha de 'd de B de Y' a 'YYYY-MM-DD'.
    """
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d de %B de %Y")
    return fecha_nacimiento.strftime("%Y-%m-%d")

# Calcula la edad de una persona a partir de su fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    """
    Calcula cuántos años tiene una persona según su fecha de nacimiento.
    """
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Procesa la lista de usuarios para eliminar duplicados y calcular edades
def procesar_usuarios(usuarios):
    """
    Procesa una lista de usuarios, eliminando duplicados y calculando edades.
    """
    usuarios_procesados = []
    usuarios = eliminar_duplicados_y_sumar_saldos(usuarios)
    
    for usuario in usuarios:
        nombre, apellido_paterno, apellido_materno = separar_nombre(usuario["nombre_completo"])
        fecha_nacimiento_formateada = formatear_fecha(usuario["fecha_nacimiento"])
        edad_actual = calcular_edad(fecha_nacimiento_formateada)
        saldo_actual = usuario["saldo"]
        
        usuario_procesado = {
            "Nombre": nombre,
            "Apellido_Paterno": apellido_paterno,
            "Apellido_Materno": apellido_materno,
            "Fecha_Nacimiento": fecha_nacimiento_formateada,
            "Edad_Actual": edad_actual,
            "Saldo_Actual": saldo_actual
        }
        usuarios_procesados.append(usuario_procesado)
    
    return usuarios_procesados

# Imprime la información de los usuarios procesados
def imprimir_usuarios(usuarios_procesados):
    """
    Muestra la información de los usuarios de manera clara y sencilla.
    """
    for usuario in usuarios_procesados:
        print(f'{usuario["Nombre"]} {usuario["Apellido_Paterno"]} {usuario["Apellido_Materno"]} nació en {usuario["Fecha_Nacimiento"]} tiene actualmente {usuario["Edad_Actual"]} años y un saldo de {usuario["Saldo_Actual"]} MXN')

# Función principal que se ejecuta al correr el script
def main():
    """
    Carga los datos de un archivo JSON, los procesa y muestra la información.
    """
    with open('C:/Users/aleja/Downloads/procesar_usuarios/Saldos_Usuarios.json', 'r') as file:
        usuarios = json.load(file)
        
    usuarios_procesados = procesar_usuarios(usuarios)
    imprimir_usuarios(usuarios_procesados)

# Ejecuta la función principal si se corre este archivo directamente
if __name__ == "__main__":
    main()
