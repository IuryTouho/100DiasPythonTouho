from flask import Flask,make_response,jsonify,request
from bd import Carros


app = Flask('Carro')
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros',methods=['GET'])
def get_carros():
    return make_response(
        jsonify(Carros)
    )

@app.route('/carros',methods=['POST'])
def create_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(carro) 
    ) 

app.run()


