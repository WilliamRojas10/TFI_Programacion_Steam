from abb import ArbolBinarioBusqueda

class Usuario:
    def __init__(self, id: int, correo_electronico: str,contrasenia: str, nombre: str, apellido: str, telefono: int, codigo_postal: int, pais: str, num_tarjeta = 0)->None:
        self.id = id #clave primaria
        self.correo_electronico = correo_electronico
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido= apellido
        self.telefono = telefono
        self.num_tarjeta = num_tarjeta
        self.codigo_postal = codigo_postal
        self.pais = pais

class Juego:
  def __init__(self,id_juego:int, titulo:str, categoria:str, anio_lanzamiento:int, desarrollador:str, franquicia:str,editor:str, precio:float)-> None:
        self.id_juego = id_juego
        self.titulo = titulo
        self.categoria = categoria
        self.anio_lanzamiento = anio_lanzamiento
        self.desarrollador = desarrollador
        self.franquicia = franquicia
        self.editor = editor
        self.precio = precio

class Carrito:
    def __init__(self, fecha:str, precio_total:float, vendido:bool)-> None:
        self.fecha = fecha
        self.lista_juegos = [] #Lista de objetos-nodo
        self.precio_total = precio_total
        self.vendido = vendido

class Plataforma:
    def __init__(self)->None:
        self.usuarios = ArbolBinarioBusqueda()
        self.juegos= ArbolBinarioBusqueda()

    def crear_usuario(self, id, correo_electronico, contrasenia, nombre, apellido,telefono, num_tarjeta, codigo_postal, pais):
        usuario = Usuario(id, correo_electronico, contrasenia, nombre, apellido,telefono, num_tarjeta, codigo_postal, pais)
        self.usuarios.agregar(id, usuario)

    def agregar_juego(self, id_juego, titulo: str, categoria: str, anio_lanzamiento: int, desarrollador: str, franquicia: str, editor: str, precio: float):
        juego = Juego(id_juego, titulo, categoria, anio_lanzamiento, desarrollador, franquicia, editor, precio)
        self.juegos.agregar(id_juego, juego)
        print (f'{titulo} agregado')

    def buscar_juego(self, titulo):
        for id in self.juegos:
            if self.juegos.obtener(id).titulo == titulo:
                print(self.juegos.obtener(id))
    #LOURDES
    def mostrar_juego(self)->None: #LOURDES
        for juego in self.juegos:
            print(self.juegos.obtener(juego))

    def eliminar_usuario(self, id): #LOURDES
        self.usuarios.eliminar(id)

    def mostrar_usuario(self)->None:
        for id in self.usuarios:
          print(self.usuarios.obtener(id))

#test: simulacion - accion - terror -> categoria 
steam = Plataforma()
steam.agregar_juego(1, 'Counter', 'Accion', 2014, 'yo', 'counter strike', 'matias', 2345 )

steam.buscar_juego('Counter')
