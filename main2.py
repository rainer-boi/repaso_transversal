#########################################################################################
# Clínica Veterinaria
# Servicios = [nombre servicio, categoría, duración min, nivel urgencia, especialista, requiere ayuno previo]
servicios = {
    'S01': ['Consulta General', 'Medicina', 30, 'Baja', 'Dra. Inés Ruiz', False],
    'S02': ['Cirugía Mayor', 'Cirugía', 120, 'Alta', 'Dr. Hugo Silva', True],
    'S03': ['Limpieza Dental', 'Estética', 60, 'Media', 'Dra. Inés Ruiz', True],
    'S04': ['Radiografía Digital', 'Diagnóstico', 40, 'Media', 'Dr. Hugo Silva', False],
    'S05': ['Vacunación Anual', 'Prevención', 15, 'Baja', 'Dra. Inés Ruiz', False]
}

# Comercial_Servicios = [valor servicio, cupos diarios disponibles]
comercial_servicios = {
    'S01': [140000, 5],
    'S02': [85000, 8],
    'S03': [100000, 10],
    'S04': [130000, 14],
    'S05': [96000, 8]
}
#########################################################################################
#1#
def sumar_servicios_por_nivel(nivel):
    suma=0
    for clave,valor in servicios.items():
        if valor[3].lower()==nivel.lower():
            suma+=comercial_servicios[clave][0]
    if suma==0:
        print("No existen servicios con este nivel")
    else:
        print(f"La suma de servicios del nivel {nivel} es {suma}")

#2#
def listado_servicios_rango_precio(minimo,maximo):
    lista=[]
    for clave,valor in servicios.items():
        if valor[0]>=minimo and valor[0]<=maximo and valor[1]>0:
            nombre=servicios[clave][0]
            doctor=servicios[clave][4]
            lista.append([nombre+"-"+doctor])
        if len(lista)>0:
            lista.sort()
            print(lista)
        else:
            print("No existen servicios entre los valores")

#3#
def actualizar_precio(codigo,nuevo_precio):
    if codigo in comercial_servicios:
        comercial_servicios[codigo][0]=nuevo_precio
        return True
    return False

#########################################################################################
#Validaciones#
def ValidarCodigo(codigo):
    if len(codigo.strip())==3:
        return True
    return False

def ValidaNombre(nombre):
    if len(nombre.strip())>=2:
        return True
    return False

def ValidaCategoria(cate):
    if len(cate.strip())==5:
        return True
    return False

def ValidaDuracion(dura):
    try:
        d=int(dura)
        if d>=10 and d<=90:
            return True
        return False
    except:
        return False

def ValidaNivel(nivel):
    if nivel.lower() in ("bajo","medio","alto"):
        return True
    return False

def ValidaDoctor(doctor):
    if len(doctor.strip())>=2:
        return True
    return False

def ValidaAyuno(ayuno):
    if ayuno.lower() in ("s","n"):
        return True
    return False

def ValidaPrecio(precio):
    try:
        p=int(precio)
        if p>=10000 and p<=180000:
            return True
        return False
    except:
        return False

def ValidaCupos(cupos):
    try:
        c=int(cupos)
        if c>0:
            return True
        return False
    except:
        return False
#########################################################################################
#4#
def agregar(codigo,serv,cate,dur,nivel,doctor,ayuno,precio,cupos):
    if codigo.upper() in servicios:
        return False
    if ayuno.lower()=="s":
        ayuno_servicio=True
    else:
        ayuno_servicio=False
    servicios[codigo]=[serv,cate,int(dur),nivel,doctor,ayuno_servicio]
    comercial_servicios[codigo]=[int(precio),int(cupos)]
    print(servicios)
    print(comercial_servicios)
    return True

#5#
def eliminar_servicio(codigo):
    if codigo in servicio:
        del comercial_servicios[codigo]
        del servicio[codigo]
        return True
    return False

#6#
#Jajanosesalu2
#########################################################################################
#menu
def menu():
    print('''
        ==Clínica veteriniaria==
        1.- Sumar servicios por nivel
        2.- Listado de servicios por rango de precios
        3.- Actualizar Precio de Servicio
        4.- Agregar servicio
        5.- Eliminar servicio
        6.- Visualizar los datos
        7.- Salir
        ''')

def seleccione():
    try:
        opcion=int(input("Seleccione: "))
        return op
    except:
        return 0

while True:
    menu
    op=seleccione()
    match op:
        case 1:
            while True:
                nivel=input("Ingrese el nivel: ")
                sumar_servicios_por_nivel(nivel)
                resp=input("Desea repetir el proceso? (s/n): ").lower()
                if resp=="n":
                    break
        case 2:
            while True:
                try:
                    minimo=int(input("Ingrese el valor mínimo: "))
                    maximo=int(input("Ingrese el valor máximo: "))
                    if minimo<maximo and minimo>0:
                        listado_servicios_rango_precio(minimo,maximo)
                    else:
                        print("Mínimo debe ser menor al máximo")
                except:
                    print("Solo valores numéricos")
                resp=input("Desea repetir el proceso? (s/n): ").lower()
                if resp=="n":
                    break
        case 3:
            while True:
                try:
                    codigo=input("Ingrese código que desea actualizar: ")
                    precio=int(input("Ingrese nuevo precio: "))
                    if precio>0:
                        resp=actualizar_precio(codigo,precio)
                        if resp==True:
                            print("Actualizado")
                        else:
                            print("No actualizado")
                    else:
                        print("Número debe ser mayor a 0")
                except:
                    print("Ingrese número numérico")
                resp=input("Desea repetir el proceso? (s/n): ").lower()
                if resp=="n":
                    break
        case 4:
            codigo=input("Ingrese código: ").upper()
            if ValidarCodigo(codigo)==False:
                print("Código incorrecto")
                continue
            servicio=input("Ingrese servicio: ")
            if ValidaNombre(servicio)==False:
                print("Servicio no puede estar vacío")
                continue
            cate=input("Ingrese categoría: ")
            if ValidaCategoria(cate)==False:
                print("Categoría incorrecta")
                continue
            duracion=input("Ingrese duración: ")
            if ValidaDuracion(duracion)==False:
                print("Duración entre 10 y 90")
                continue
            nivel=input("Ingrese nivel: ")
            if ValidaNivel(nivel)==False:
                print("Nivel incorrecto")
                continue
            doctor=input("Ingrese especialista: ")
            if ValidaDoctor(doctor)==False:
                print("Doctor no puede estar vacío")
                continue
            ayuno=input("Ingrese ayuno (s/n): ").lower()
            if ValidaAyuno(ayuno)==False:
                print("El ayuno debe ser s o n")
                continue
            precio=input("Ingrese precio: ")
            if ValidaPrecio(precio)==False:
                print("El precio es incorrecto")
                continue
            cupos=input("Ingrese cupos: ")
            if ValidaCupos(cupos)==False:
                print("Cupos debe ser mayor a 0")
                continue
            resp=agregar
        case 5:
            while True:
                codigo=input("Ingrese servicio a eliminar").strip().lower()
                resp=eliminar_servicio(codigo)
                if resp==True:
                    print("Elimino servicio")
                else:
                    print("No elimino servicio")
                resp=input("Desea repetir el proceso? (s/n): ").lower()
                if resp in ("n"):
                    break
        case 7:
            print("Adiós.")
            break