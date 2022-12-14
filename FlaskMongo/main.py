from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

from Controladores.PartidoControlador import PartidoControlador

app = Flask(__name__)
cors = CORS(app)

################################
##     Variables globales     ##
################################

miControladorPartido = PartidoControlador()


################################
##     Probar el Servicio     ##
################################

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "-- Server Running... --"
    return jsonify(json)

################################
##     Endpoint Partidos      ##
################################

#index
@app.route("/partidos", methods = ["GET"])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

#Crea partido
@app.route("/partidos", methods = ["POST"])
def crearPartido():
    print("crear partido")
    data = request.get_json()
    print("data", data)
    json = miControladorPartido.create(data)
    print("json",json)
    return jsonify(json)

#Para mirar documentos
@app.route("/partidos/<string:id>", methods = ["GET"])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

#para actualizar los partidos
@app.route("/partidos/<string:id>", methods = ["PUT"])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

#para eliminar partidos
@app.route("/partidos/<string:id>", methods = ["DELETE"])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)
