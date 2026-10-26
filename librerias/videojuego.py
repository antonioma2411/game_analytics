
class Videojuego:
    def __init__(self,id_juego,titulo,genero,precio,horas_jugadas,valoracion):
        self.id=id_juego
        self.titulo = titulo
        self.genero = genero
        self.precio = float(precio) #validamos que sea un float
        self.horas_jugadas = float(horas_jugadas) #validamos que sea un float
        self.valoracion = float(valoracion) #validamos que sea un float
        
    def obtenerCategoriaPrecio (self):
        if self.precio<20:
            return "Economico"
        elif self.precio <=40:
            return "Medio"
        else:
            return "Premium"

    def obtenerNivelDedicacion (self):
        if self.horas_jugadas<50:
            return "Casual"
        elif self.horas_jugadas <=150:
            return "Habitual"
        else:
            return "Experto"

    def filaCSV (self):

        #Devuelve la fila con los datos cambiados
        return [
            self.id,
            self.titulo,
            self.titulo,
            self.genero,
            self.obtenerCategoriaPrecio(),
            self.obtenerNivelDedicacion(),
            self.valoracion
        ]



