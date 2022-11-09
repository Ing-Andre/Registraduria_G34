from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

################################
##     Probar el Servicio     ##
################################

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "-- Server Running... --"
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)