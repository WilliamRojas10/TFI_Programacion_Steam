from abb import ArbolBinarioBusqueda
#WILLIAM

class Usuario:
    def __init__(self, dni: int, correo_electronico: str,contrasenia: str, nombre: str, apellido: str, telefono: int, codigo_postal: int, pais: str, num_tarjeta = 0)->None:
        self.dni = dni #clave primaria
        self.correo_electronico = correo_electronico
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido= apellido
        self.telefono = telefono
        self.num_tarjeta = num_tarjeta
        self.nombre_tarjeta = ""
        self.codigo_postal = codigo_postal
        self.pais = pais
        self.biblioteca = [] #lista de juegos

    def __str__(self):
        return "DNI: {0}\ncorreo_electronico: {1}\ncontrasenia: {2}\nnombre: {3}\napellido: {4}\ntelefono: {5}\ncodigo_postal{6}\npais: {7}\nnumero_tarjeta: {8}\n" \
            .format(self.dni,self.correo_electronico,self.contrasenia,self.nombre,self.apellido,self.telefono,self.codigo_postal,self.pais,self.num_tarjeta)

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

  def __str__(self):
       return "Título: {1}\nCategoría: {2}\nAño de lanzamiento: {3}\nDesarrollador: {4}\nFranquicia: {5}\nEditor: {6}\nPrecio: ${7}"\
        .format(self.id_juego,self.titulo,self.categoria,self.anio_lanzamiento,self.desarrollador,self.franquicia,self.editor,self.precio)

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

    def longitud (self, abb):
        return abb.longitud()
    def _juegos (self)-> ArbolBinarioBusqueda:
        return self.juegos
    def _usuarios (self)-> ArbolBinarioBusqueda:
        return self.juegos

    #METODOS PARA USUARIO
    def crear_usuario(self, dni, nombre, apellido,telefono, correo_electronico, contrasenia, pais, codigo_postal):#WILLIAM
        usuario = Usuario(dni, correo_electronico, contrasenia, nombre, apellido,telefono, codigo_postal, pais)
        self.usuarios.agregar(dni, usuario)

    def get_usuario(self, dni, num_tarjeta:int, nombre_tarjeta)->None:
        self.usuarios[dni].num_tarjeta = num_tarjeta
        self.usuarios[dni].nombre_tarjeta = nombre_tarjeta

    def eliminar_usuario(self, dni): #LOURDES
        self.usuarios.eliminar(dni)

    def mostrar_usuarios(self)->None: #LOURDES
        for dni in self.usuarios:
          print(self.usuarios.obtener(dni))

    def contiene_usuario(self,correo_electronico, contrasenia):
        encontrado = False
        for nodo in self.usuarios:
            if self.usuarios.obtener(nodo).correo_electronico == correo_electronico and self.usuarios.obtener(nodo).contrasenia == contrasenia:
                encontrado = True
            else:
                encontrado = False
        return encontrado

    #METODOS PARA JUEGOS
    def agregar_juego(self, id_juego, titulo: str, categoria: str, anio_lanzamiento: int, desarrollador: str, franquicia: str, editor: str, precio: float):#TAMARA
        juego = Juego(id_juego, titulo, categoria, anio_lanzamiento, desarrollador, franquicia, editor, precio)
        self.juegos.agregar(id_juego, juego)
        print (f'{titulo} agregado')

    def eliminar_juego(self, id_juego):#TAMARA
        self.juegos.eliminar(id_juego)

    def mostrar_juegos(self)->None: #WILLIAM
        for juego in self.juegos:
            print(self.juegos.obtener(juego).id_juego, "->", self.juegos.obtener(juego).titulo)
            
    def buscar_juego(self, titulo):#WILLIAM
        encontrado = False
        for id in self.juegos:
            if self.juegos.obtener(id).titulo == titulo:
                encontrado = True
                return (self.juegos.obtener(id))
        if encontrado != True:
            print(f"No se encontró {titulo}")
    
    def comprar_juego(self, dni, titulo):
        comprado = False
        for id in self.juegos:
            if self.juegos.obtener(id).titulo == titulo:
                juego = self.juegos.obtener(id)
                self.usuarios.obtener(dni).biblioteca.append(juego)
                comprado = True
        return comprado
    def mostrar_biblioteca(self, dni):
        for juego in range(0, len(self.usuarios.obtener(dni).biblioteca)):
            print(f"{juego +1} -> {self.usuarios.obtener(dni).biblioteca[juego].titulo}")


#test
"""
steam = Plataforma()
juego = Juego(1, 'counter', 'accion', 2012, 'yo', 'unity', 'matias', 2550)
steam.crear_usuario(4, "w", "r", 3, "ww", "rr", "a", 5)
steam.usuarios.obtener(4).biblioteca.append(juego)
steam.mostrar_biblioteca(4)
print(steam.usuarios.obtener(4).biblioteca)
                            # indice juego
#steam.agregar_juego(1, 'counter', 'accion', 2012, 'yo', 'unity', 'matias', 2550)
steam.mostrar_juegos()
#steam.crear_usuario(4, "w", "r", 3, "ww", "rr", "a", 5)
steam.comprar_juego(4, "counter")
#IMPRIMIR EL JUEGO QUE ESTA EN BIBLIOTECA
#print(steam.usuarios.obtener(4).biblioteca[0].titulo)

#steam.mostrar_biblioteca(4)"""