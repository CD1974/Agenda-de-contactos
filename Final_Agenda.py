class Direccion:
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""
    def GetCalle(self):
        return self.__Calle
    def GetPiso(self):
        return self.__Piso
    def GetCiudad(self):
        return self.__Ciudad
    def GetCodigoPostal(self):
        return self.__CodigoPostal
    def SetCalle(self,calle):
        self.__Calle = calle
    def SetPiso(self,piso):
        self.__Piso = piso
    def SetCiudad(self,ciudad):
        self.__Ciudad = ciudad
    def SetCodigoPostal(self,codigopostal):
        self.__CodigoPostal = codigopostal

class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaNacimiento = ""
    def GetNombre(self):
        return self.__Nombre
    def GetApellidos(self):
        return self.__Apellidos
    def GetFechaNacimiento(self):
        return self.__FechaNacimiento
    def SetNombre(self,nombre):
        self.__Nombre = nombre
    def SetApellidos(self,apellidos):
        self.__Apellidos = apellidos
    def SetFechaNacimiento(self,fechanacimiento):
        self.__FechaNacimiento = fechanacimiento

class Teléfono:
    def __init__(self):
        self.__TeléfonoMóvil = ""
        self.__TeléfonoFijo = ""
        self.__TeléfonoTrabajo = ""
    def GetTeléfonoMóvil(self):
        return self.__TeléfonoMóvil
    def GetTeléfonoFijo(self):
        return self.__TeléfonoFijo
    def GetTeléfonoTrabajo(self):
        return self.__TeléfonoTrabajo
    def SetTeléfonoMóvil(self,móvil):
        self.__TeléfonoMóvil = móvil
    def SetTeléfonoFijo(self,fijo):
        self.__TeléfonoFijo = fijo
    def SetTeléfonoTrabajo(self,trabajo):
        self.__TeléfonoTrabajo = trabajo

class Contacto(Persona,Direccion,Teléfono):
    def __init__(self):
        self.__Email = ""
    def GetEmail(self):
        return self.__Email
    def SetEmail(self,email):
        self.__Email = email
    def MostrarContacto(self):
        print("-----Contacto-----")
        print("Nombre:",self.GetNombre())
        print("Apellidos:",self.GetApellidos())
        print("Fecha de Nacimiento:",self.GetFechaNacimiento())
        print("Teléfono móvil:",self.GetTeléfonoMóvil())
        print("Teléfono Fijo:",self.GetTeléfonoFijo())
        print("Teléfono Trabajo:",self.GetTeléfonoTrabajo())
        print("Calle:",self.GetCalle())
        print("Piso:",self.GetPiso())
        print("Ciudad:",self.GetCiudad())
        print("Código Postal:",self.GetCodigoPostal())
        print("Email:",self.__Email)
        print("----------")

class Agenda:
    def __init__(self,path):
        self.__ListaContactos = []
        self.__Path = path
    def CargarContactos(self):
        try:
            fichero = open(self.__Path,"r")
        except:
            print("ERROR: No existe el fichero de la agenda")
        else:
            contactos = fichero.readlines()
            fichero.close()
            if(len(contactos)>0):
                for contacto in contactos:
                    datos = contacto.split("#")
                    if(len(datos)==11):
                        nuevocontacto = Contacto()
                        nuevocontacto.SetNombre(datos[0])
                        nuevocontacto.SetApellidos(datos[1])
                        nuevocontacto.SetFechaNacimiento(datos[2])
                        nuevocontacto.SetTeléfonoMóvil(datos[3])
                        nuevocontacto.SetTeléfonoFijo(datos[4])
                        nuevocontacto.SetTeléfonoTrabajo(datos[5])
                        nuevocontacto.SetCalle(datos[6])
                        nuevocontacto.SetPiso(datos[7])
                        nuevocontacto.SetCiudad(datos[8])
                        nuevocontacto.SetCodigoPostal(datos[9])
                        nuevocontacto.SetEmail(datos[10])
                        self.__ListaContactos = self.__ListaContactos + [nuevocontacto]
                print("INFO: Se han cargado un total de ",len(self.__ListaContactos),"contactos")
    def CrearNuevoContacto(self,nuevocontacto):
        self.__ListaContactos = self.__ListaContactos + [nuevocontacto]
    def GuardarContactos(self):
        try:
            fichero = open(self.__Path,"w")
        except:
            print("ERROR: No se puede guardar.")
        else:
            for contacto in self.__ListaContactos:
                texto = contacto.GetNombre() + "#"
                texto = texto + contacto.GetApellidos() + "#"
                texto = texto + contacto.GetFechaNacimiento() + "#"
                texto = texto + contacto.GetTeléfonoMóvil() + "#"
                texto = texto + contacto.GetTeléfonoFijo() + "#"
                texto = texto + contacto.GetTeléfonoTrabajo() + "#"
                texto = texto + contacto.GetCalle() + "#"
                texto = texto + contacto.GetPiso() + "#"
                texto = texto + contacto.GetCiudad() + "#"
                texto = texto + contacto.GetCodigoPostal() + "#"
                texto = texto + contacto.GetEmail() + "\n"
                fichero.write(texto)
            fichero.close()
    def MostrarAgenda(self):
        print("########## AGENDA ##########")
        print("Número de contactos: ",len(self.__ListaContactos))
        for contacto in self.__ListaContactos:
            contacto.MostrarContacto()
            print("###############################")
    def BuscarContactoPorNombre(self,nombre):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() == nombre:
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados
    def BuscarContactoPorTeléfono(self,teléfono):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTeléfonoMóvil() == teléfono
                or contacto.GetTeléfonoFijo() == teléfono
                or contacto.GetTeléfonoTrabajo() == teléfono):
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados
    def BorrarContactoPorNombre(self,nombre):
        listafinal = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() != nombre:
                listafinal = listafinal + [contacto]
        print("Info: ", len(self.__ListaContactos) - len(listafinal)," contactos han sido borrados")
        self.__ListaContactos = listafinal
    def BorrarContactoPorTeléfono(self,teléfono):
        listafinal = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTeléfonoMóvil() == teléfono
                or contacto.GetTeléfonoFijo() == teléfono
                or contacto.GetTeléfonoTrabajo() == teléfono):
                listafinal = listafinal + [contacto]
        print("Info: ", len(self.__ListaContactos) - len(listafinal)," contactos han sido borrados")
        self.__ListaContactos = listafinal

def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Error: Tienes que introducir un número.")
        else:
            leido = True
        return numero

def MostrarMenu():
    print("""Menú
1)Mostrar Contactos
2)Buscar Contactos
3)Crear Contacto Nuevo
4)Borrar Contacto
5)Guardar Contactos
6)Salir""")

def BuscarContactos(agenda):
    print("""Buscar Contactos:
1)Nombre
2)Teléfono
3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            encontrados = agenda.BuscarContactoPorNombre(input((">Introduce el nombre a buscar:")))
            if len(encontrados) > 0:
                print("########## CONTACTOS ENCONTRADOS ##########")
                for item in encontrados:
                    item.MostrarContacto()
                print("#######################################")
            else:
                print("INFO: No se han encontrado contactos.")
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = agenda.BuscarContactoPorTeléfono(input((">Introduce el teléfono a buscar:")))
            if len(encontrados) > 0:
                print("########## CONTACTOS ENCONTRADOS ##########")
                for item in encontrados:
                    item.MostrarContacto()
                print("########################################")
            else:
                print("INFO: No se han encontrado contactos.")
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def ProcesoCrearContacto(agenda):
    nuevocontacto = Contacto()
    nuevocontacto.SetNombre(input((">Introduce el nombre del contacto: ")))
    nuevocontacto.SetApellidos(input((">Introduce los apellidos del contacto:")))
    nuevocontacto.SetFechaNacimiento(input((">Introduce la fecha de nacimiento del contacto:")))
    nuevocontacto.SetTeléfonoMóvil(input((">Introduce el teléfono móvil del contacto:")))
    nuevocontacto.SetTeléfonoFijo(input((">Introduce el teléfono fijo del contacto:")))
    nuevocontacto.SetTeléfonoTrabajo(input((">Introduce el teléfono del trabajo del cpntacto")))
    nuevocontacto.SetCalle(input((">Introduce la calle de la dirección del contacto:")))
    nuevocontacto.SetPiso(input((">Introduce el piso de la dirección del contacto:")))
    nuevocontacto.SetCiudad(input((">Introduce la ciudad de la dirección del contacto:")))
    nuevocontacto.SetCodigoPostal(input((">Introduce el código postal de la dirección del contacto:")))
    nuevocontacto.SetEmail(input((">Introduce el @email del contacto:")))
    agenda.CrearNuevoContacto(nuevocontacto)
def BorrarContacto(agenda):
    print("""Buscar contactos a borrar por:
1)Nombre
2)Teléfono
3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            agenda.BorrarContactoPorNombre(input((">Introduce el nombre a borrar:")))
            finbuscar = True
        elif opcbuscar == 2:
            agenda.BorrarContactoPorTeléfono(input((">Introduce el teléfono a borrar:")))
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def Main():
    agenda = Agenda(r"C:\Users\mjcd1\OneDrive\Escritorio\agenda.txt")
    agenda.CargarContactos()
    fin = False
    while not(fin):
        MostrarMenu()
        opc = ObtenerOpcion("Opción:")
        if opc == 1:
            agenda.MostrarAgenda()
        elif opc == 2:
            BuscarContactos(agenda)
        elif opc == 3:
            ProcesoCrearContacto(agenda)
        elif opc == 4:
            BorrarContacto(agenda)
        elif opc == 5:
            agenda.GuardarContactos()
        elif opc == 6:
            fin = 1
Main()