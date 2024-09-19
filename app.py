from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:nati_id>', methods=['GET'])
def enosh(nati_id)
    return jsonify()

if __name__ == '__main__':
    app.register_blueprint(player_blueprint, url_p)