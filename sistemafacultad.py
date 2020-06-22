##Este programa almacena datos de alumnos de una universidad, permite agregar, buscar, eliminar e imprimir usuarios.

import os
##La totalidad de alumnos y sus datos se almacenarán en una lista de diccionarios llamada alumnos
alumnos=[]
##La tupla comentada, es una tupla mas acorde a la realidad, pero que dificulta pruebas durante el desarrollo
##La tupla contiene los datos que darán forma al diccionario que tendrá los datos de cada alumno de una facultad
##datos=('legajo','nombre','apellido','dni','carrera','sede','mail','telefono')
datos=('legajo','nombre')

##Como se imprime en reiteradas ocasiones una línea para separar usuarios, almacenamos un string con guiones
guiones='-------------------------------------'
ingreso=''

def agregarAlumno():
    alumno={}
    
    for dato in datos:
        print("Ingrese "+dato+" del alumno")
        alumno[dato]=input().title()
    alumnos.append(alumno)
    print(alumnos)



def consultaAlumno():
    parametro=''
    val=''
    
    mensaje='\nBajo que parametro desea buscar al alumno?\n'
    mensaje+=str(datos)
    mensaje+='\n'
       
    parametro=input(mensaje)
    
    if parametro in datos:

        val=input('Ingrese '+parametro+' a buscar')
        
        for alumno in alumnos:
            for llave, valor in alumno.items():
                if alumno[llave].lower()==val.lower():
                    print(guiones)
                    for llave, valor in alumno.items():
                        print(llave.title() + ': \t' + valor.title())
                    print(guiones)
    else:
        print("Ese parametro de busqueda no existe")


def imprimirAlumnos():
    print(guiones)
    for alumno in alumnos:
        for llave, valor in alumno.items():
            print(llave.title() + ': \t' + valor.title())
        print(guiones)

os.system ("cls")   ##borro basura de consola

while ingreso!='*':
     
    ingreso=str(input("Que desea hacer?\na: agregar alumno\tc:consultar por alumno\nb:borrar alumno\t\ti:imprimir alumnos\nIngrese * para salir\n"))
    os.system ("cls")   ##borro basura de consola

    if ingreso.lower()=='a':
        agregarAlumno()
  ##      os.system ("cls")   ##borro basura de consola
    
    if ingreso.lower()=='c':
        consultaAlumno()
    
    if ingreso.lower()=='b':
        borrarAlumno()
  ##      os.system ("cls")   ##borro basura de consola
        
    if ingreso.lower()=='i':
  ##      os.system ("cls")   ##borro basura de consola
        imprimirAlumnos()
    
        
##os.system ("cls")   ##borro basura de consola       
print("Fin del programa")
