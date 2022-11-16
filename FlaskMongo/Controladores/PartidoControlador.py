from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Partido import Partido 

class PartidoControlador():
    #Constructor
    def __init__(self):
        self.repositorioPartido = PartidoRepositorio()

    #Devuelve todos los documentos de la colección
    def index(self):
        return self.repositorioPartido.findAll()

    #Crea documentos
    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    #Muestra documento
    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    #Actualizar
    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual,nombre = infoPartido["nombre"]
        PartidoActual,lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)
        