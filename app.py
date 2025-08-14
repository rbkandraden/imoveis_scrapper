from flask import Flask, jsonify, request, render_template
from sites.olx import buscar_imoveis_olx

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imoveis/olx', methods=['GET'])
def imoveis_olx():
    cidade = request.args.get('cidade')
    estado = request.args.get('estado')
    max_preco = request.args.get('max_preco', type=int)
    if not cidade or not estado or not max_preco:
        return jsonify({'erro': 'Informe cidade, estado e preço máximo'}), 400
    resultados = buscar_imoveis_olx(cidade, estado, max_preco)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
