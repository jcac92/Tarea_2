
######################### Importación de Librerías ######################### 

from Tkinter import *       #importar librería gráfica TkInter
import tkMessageBox         #importar el módulo para los mensajes de alerta, pregunta etc.
import os                   #importar la clase os, que ayuda a cerrar ventanas desde funciones
from pyswip import Functor, Variable, Query, call, Prolog


######################### Declaración Variables Globales ######################### 

global LabelInsertar
global LabelConsultar
global principal

global EntryComida
global EntryNombre
global OpcionSexo
global EntryEco
global EntryEdad
global EntryRaza

global EntryComidaC
global EntryNombreC
global OpcionSexoC
global EntryEcoC
global EntryEdadC
global EntryRazaC

global RazaInsertar
global EdadInsertar
global GeneroInsertar
global NombreInsertar
global EcosistemaInsertar
global ComidaInsertar

global A
global B
global C
global D
global E
global F

######################### Logica de Prolog #########################    

prolog = Prolog()

assertz = Functor("assertz", 1)
animal = Functor("animal", 6)

Raza = Variable()
Edad = Variable()
Genero = Variable()
Nombre = Variable()
Ecosistema = Variable()
Comida = Variable()

A = Variable()
B = Variable()
C = Variable()
D = Variable()
E = Variable()
F = Variable()

q = Variable()

def consultarBC(Raza, Edad,Genero,Nombre,Ecosistema,Comida):
    print "Consultando..."
    q = Query(animal(Raza,Edad,Genero,Nombre,Ecosistema,Comida))
    while q.nextSolution():
        print "Hello,",Raza.value, Edad.value, Genero.value, Nombre.value, Ecosistema.value, Comida.value

def insertarBC(RazaInsertar, EdadInsertar, GeneroInsertar, NombreInsertar, EcosistemaInsertar, ComidaInsertar):
    print RazaInsertar
    print "insertando...\n"
    prolog.assertz("animal("+RazaInsertar+","+EdadInsertar+","+GeneroInsertar+","+NombreInsertar+","+EcosistemaInsertar+","+ComidaInsertar+")")

    print "consultando...\n"
    consultarBC(A, B, C, D, E, F)


######################### Funciones de Programa #########################    

def FrameConsultar():
    global LabelInsertar
    global LabelConsultar
    global principal

    global EntryComidaC
    global EntryNombreC
    global OpcionSexoC
    global EntryEcoC
    global EntryEdadC
    global EntryRazaC
    
    principal.destroy()
    LabelInsertar.destroy()
    LabelConsultar = Label(lienzo, image=imagenConsultar, bg='white')
    LabelConsultar.grid( row = 0, column = 0 )

    LabelNombreC = Label(LabelConsultar, bg="white", text = "Nombre:")
    LabelNombreC.place( x=100, y=120 )
    EntryNombreC = Entry(LabelConsultar)
    EntryNombreC.place( x=160, y=120, width=120, height=20 )

    LabelSexoC = Label(LabelConsultar, bg="white", text = "Genero:")
    LabelSexoC.place( x=105, y=150 )
    optionesSexoC = ("femenino", "masculino")
    defaultOptionC = StringVar()
    OpcionSexoC = apply(OptionMenu, (LabelConsultar, defaultOptionC) + optionesSexoC)
    defaultOptionC.set("")
    OpcionSexoC["width"] = 15
    OpcionSexoC.place( x=160, y=150, width=120, height=20 )
    
    LabelRazaC = Label(LabelConsultar, bg="white", text = "Raza:")
    LabelRazaC.place( x=120, y=180 )
    EntryRazaC = Entry(LabelConsultar)
    EntryRazaC.place( x=160, y=180, width=120, height=20 )

    LabelEdadC = Label(LabelConsultar, bg="white", text = "Edad:")
    LabelEdadC.place( x=117, y=210 )
    EntryEdadC = Entry(LabelConsultar)
    EntryEdadC.place( x=160, y=210, width=120, height=20 )

    LabelEcoC = Label(LabelConsultar, bg="white", text = "Ecosistema:")
    LabelEcoC.place( x=80, y=240 )
    EntryEcoC = Entry(LabelConsultar)
    EntryEcoC.place( x=160, y=240, width=120, height=20 )

    LabelComidaC = Label(LabelConsultar, bg="white", text = "Comida Favorita:")
    LabelComidaC.place( x=50, y=270 )
    EntryComidaC = Entry(LabelConsultar)
    EntryComidaC.place( x=160, y=270, width=120, height=20 )

    BotonConsultar = Button(LabelConsultar, text = "Consultar", width = "15", command= Consultar ) #Botón para registrar nuevos empleados
    BotonConsultar.place(x=350, y=230, width=70, height=25)

def Consultar():
##    global Raz
##    global Ed
##    global Gen
##    global Nomb
##    global Eco
##    global ComFaf
    global EntryComidaC
    global EntryNombreC
    global OpcionSexoC
    global EntryEcoC
    global EntryEdadC
    global EntryRazaC
    var = OpcionSexoC.cget("text")
    A = Variable()
    B = Variable()
    C = Variable()
    D = Variable()
    E = Variable()
    F = Variable()
    if EntryRazaC.get() == "":
        RazaC = "A"
    else:
        RazaC = EntryRazaC.get()
        
    if EntryEdadC.get() == "":
        EdadC = "B"
    else:
        EdadC = EntryEdadC.get()
        
    if var == "":
        var = "C"
        
    if EntryNombreC.get() == "":
        NombreC = "D"
    else:
        NombreC = EntryNombreC.get()
        
    if EntryEcoC.get() == "":
        EcoC = "E"
    else:
        EcoC = EntryEcoC.get()
        
    if EntryComidaC.get() == "":
        ComidaC = "F"
    else:
        ComidaC = EntryComidaC.get()
        
    consultarBC(RazaC, EdadC, var, NombreC, EcoC, ComidaC)

def FrameInsertar():
    global LabelInsertar
    global LabelConsultar
    global principal

    global EntryComida
    global EntryNombre
    global OpcionSexo
    global EntryEco
    global EntryEdad
    global EntryRaza
    
    principal.destroy()
    LabelConsultar.destroy()
    LabelInsertar = Label(lienzo, image=imagenInsertar, bg='white')
    LabelInsertar.grid( row = 0, column = 0 )

    LabelNombre = Label(LabelInsertar, bg="white", text = "Nombre:")
    LabelNombre.place( x=100, y=120 )
    EntryNombre = Entry(LabelInsertar)
    EntryNombre.place( x=160, y=120, width=120, height=20 )

    LabelSexo = Label(LabelInsertar, bg="white", text = "Genero:")
    LabelSexo.place( x=105, y=150 )
    optionesSexo = ("femenino", "masculino")
    defaultOption = StringVar()
    OpcionSexo = apply(OptionMenu, (LabelInsertar, defaultOption) + optionesSexo)
    defaultOption.set("masculino")
    OpcionSexo["width"] = 15
    OpcionSexo.place( x=160, y=150, width=120, height=20 )
    
    LabelRaza = Label(LabelInsertar, bg="white", text = "Raza:")
    LabelRaza.place( x=120, y=180 )
    EntryRaza = Entry(LabelInsertar)
    EntryRaza.place( x=160, y=180, width=120, height=20 )

    LabelEdad = Label(LabelInsertar, bg="white", text = "Edad:")
    LabelEdad.place( x=117, y=210 )
    EntryEdad = Entry(LabelInsertar)
    EntryEdad.place( x=160, y=210, width=120, height=20 )

    LabelEco = Label(LabelInsertar, bg="white", text = "Ecosistema:")
    LabelEco.place( x=80, y=240 )
    EntryEco = Entry(LabelInsertar)
    EntryEco.place( x=160, y=240, width=120, height=20 )

    LabelComida = Label(LabelInsertar, bg="white", text = "Comida Favorita:")
    LabelComida.place( x=50, y=270 )
    EntryComida = Entry(LabelInsertar)
    EntryComida.place( x=160, y=270, width=120, height=20 )

    BotonInsertar = Button(LabelInsertar, text = "Registrar", width = "15", command= Insertar ) #Botón para registrar nuevos empleados
    BotonInsertar.place(x=350, y=230, width=70, height=25)

def Insertar():
    global Raz
    global Ed
    global Gen
    global Nomb
    global Eco
    global ComFaf
    global EntryComida
    global EntryNombre
    global OpcionSexo
    global EntryEco
    global EntryEdad
    global EntryRaza
    var = OpcionSexo.cget("text")
    insertarBC(EntryRaza.get(), EntryEdad.get(), var, EntryNombre.get(), EntryEco.get(), EntryComida.get())

def FrameInicio():
    global LabelInsertar
    global LabelConsultar
    global principal
    tkMessageBox.showinfo("TI-3404 JFM-ZOO", 'Bienvenido(a) a sistema\nJFM-ZOO')
    principal.destroy()
    LabelInsertar.destroy()
    LabelConsultar.destroy()
    principal = Label(lienzo, image=imagenInicio, bg='white')
    principal.grid( row=0, column=0 )

def info():
    #devolver cuadro de mensaje, con la informacion del programa
    tkMessageBox.showinfo("Acerca de...", 'JFM-ZOO\nFernanda    Melissa    Jean Carlo\nATI-TEC\nTI-3404')

def salir():
    #Salir del programa
    os._exit(100)
    

######################### Ventana Principal #########################    

raiz = Tk()
raiz.resizable( width = NO, height = NO )
raiz.title("TI-3404 JFM-ZOO")

imagenInicio = PhotoImage(file='j.gif') #Mostrar la imagen en la ventana de Bienvenida
imagenInsertar = PhotoImage(file='a.gif')
imagenConsultar = PhotoImage(file='g.gif')

lienzo = Canvas( raiz,width = 800, height = 500, bg = "white" ) #definir el canvas
lienzo.grid( row = 0, column = 0 ) #ubicarlo

principal = Label(lienzo, image=imagenInicio, bg='white')
principal.grid(row=0, column=0)#Ventana Insertar

LabelInsertar = Label()
LabelConsultar = Label()
######################### Annadir Menus #########################
    
barraMenu = Menu(raiz) #Crear la barra de menús

menuArchivo = Menu(barraMenu, tearoff = 0)
menuArchivo.add_command(label = "Salir  Alt+F4", command = salir)
barraMenu.add_cascade(label = "Archivo", menu = menuArchivo)

menuOperaciones = Menu(barraMenu, tearoff = 0)
menuOperaciones.add_command(label = "Inicio", command = FrameInicio)
menuOperaciones.add_command(label = "Inserción", command = FrameInsertar)
menuOperaciones.add_command(label = "Consulta", command = FrameConsultar)
barraMenu.add_cascade(label = "Operaciones", menu = menuOperaciones)

menuAyuda = Menu(barraMenu, tearoff = 0)
menuAyuda.add_command(label = "Acerca de", command = info)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)

raiz.config(menu = barraMenu) #Agrega los menús, a la ventana principal

#FIN DEL PROGRAMA
