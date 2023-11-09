from abb import ArbolBinarioBusqueda
import pickle


import pickle

class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni==other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni

    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)

class Pelicula():
    def __init__(self,titulo,genero,anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.alquilada = None

    def __str__(self):
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilada: {3}" \
            .format(self.titulo,self.genero,self.anio,self.alquilada)
        #return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilada(self):
        return self.alquilada != None

    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.titulo<other.titulo
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.titulo<=other.titulo
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.titulo==other.titulo
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.titulo!=other.titulo
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.titulo>other.titulo
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.titulo>=other.titulo

class Videoclub:
    def __init__(self):
        self.socios = [] #ABB
        self.peliculas = [] #ABB
    def contiene_socio(self,dni)->bool:
        esta = False
        for socio in self.socios:
            if socio.dni == dni:
                esta = True
        return esta
    def buscar_socio(self,dni)->bool:
        devolver = None
        for socio in self.socios:
            if socio.dni == dni:
                devolver = socio
        return devolver
    def alta_nuevo_socio(self,socio):
        self.socios.append(socio)

    def baja_socio(self,dni):
        socio = self.buscar_socio(dni)
        self.socios.remove(socio)

    def mostrar_socios(self):
        for socio in self.socios:
            print (socio)

    def contiene_pelicula(self,titulo):
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                esta = True
        return esta
    def buscar_pelicula(self,titulo)->"Pelicula":
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                devolver = pelicula
        return devolver
    def alta_nueva_pelicula(self,pelicula)->None:
        self.peliculas.append(pelicula)

    def baja_pelicula(self,titulo)->None:
        pelicula = self.buscar_pelicula(titulo)
        self.peliculas.remove(pelicula)

    def alquilar_pelicula(self,titulo,dni):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni

    def devolver_pelicula(self,titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada != None:
                pelicula.alquilada = None

    def guardar_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.socios = video.socios
        self.peliculas = video.peliculas
        pickle_file.close()

"""persona0 = Socio(234567890, 'guillermo', 35120108, 'pasaje caracas')
persona1 = Socio(123456789,'marcos',3517477399,'caracas')
video = Videoclub()
video.alta_nuevo_socio(persona1)
video.alta_nuevo_socio(persona0)

video.mostrar_socios()"""

#-----------------------------------------------------------
class Socio(): #Es el objeto donde se guarda los datos de un socio
    def __init__(self, dni, nombre, telefono, domicilio):
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)

class Pelicula():
    def __init__(self,id, titulo,genero,anio):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.alquilada = None
    def __str__(self):
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilada: {3}" \
            .format(self.titulo,self.genero,self.anio,self.alquilada)


class VideoClubABB():
    def __init__(self) -> None:
        self.socios = ArbolBinarioBusqueda() #ABB
        self.peliculas = ArbolBinarioBusqueda() #ABB

    def contiene_socio(self, dni)->bool:
        esta = True
        if self.socios.obtener(dni) == None: #if self.socios.obtener(dni) VARIANTE
            esta = False
        return esta

    def alta_nuevo_socio(self, dni:int , nombre:str, telefono:str, domicilio:str)-> None:
        socio = Socio(dni, nombre, telefono, domicilio) #Se crea un objeto 'socio' (se carga sus datos)
        self.socios.agregar(dni, socio)

    def baja_socio(self,dni:str)-> None:
        self.socios.eliminar(dni)

    def buscar_socio(self,dni:int)->bool:
        if self.contiene_socio(dni):
            print(self.socios.obtener(dni))
        else:
            print(f'No existe un socio con DNI: {dni}')

    def mostrar_socios(self)->None:#-> De cada socio(dni, nombre, telefono, domicilio) LOURDES
        for dni in self.socios:
            print(self.socios.obtener(dni))

    def alta_nueva_pelicula(self,id, titulo:str, genero:str, anio:int)-> None:
        pelicula = Pelicula(id, titulo, genero, anio)
        self.peliculas.agregar(id, pelicula)

    def contiene_pelicula(self, id:int)->bool: #LOURDES
        esta=True
        if self.peliculas.obtener(id)== None:
            esta= False
        return esta

    def buscar_pelicula(self, id: int):#TAMARA
        if self.contiene_pelicula(id):
            print(self.peliculas.obtener(id))
        else:
            print(f'No existe la pelicula con el id: {id}')

    def baja_pelicula(self, id:int): #TAMARA
        self.peliculas.eliminar(id)

    def alquilar_pelicula(self,titulo,dni):
        for id in self.peliculas:
            if self.peliculas[id].titulo == titulo and self.peliculas[id].alquilada == None:
                self.peliculas[id].alquilada = dni

    def devolver_pelicula(self, titulo:str): #TAMARA
        for id in self.peliculas:
            if self.peliculas[id].titulo == titulo and self.peliculas[id].alquilada != None:
                self.peliculas[id].alquilada = None

#Test
videoClub = VideoClubABB()

#Agregando socios
videoClub.alta_nuevo_socio(12345678, 'marcos', '3511234567', 'caracas 5740') #nodo raiz
videoClub.alta_nuevo_socio(23456789, 'lau', '3512222222', 'cacheuta 1234')
videoClub.mostrar_socios()
#videoClub.baja_socio(23456789)
#videoClub.buscar_socio(23456789)

videoClub.alta_nueva_pelicula(1, "Titanic", "drama", 1950)
#videoClub.buscar_pelicula(1)
#videoClub.buscar_pelicula(2)
videoClub.alquilar_pelicula("Titanic", 12345678)
videoClub.buscar_pelicula(1)
videoClub.devolver_pelicula("Titanic")
videoClub.buscar_pelicula(1)

