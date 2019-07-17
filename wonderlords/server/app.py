from flask import Flask, jsonify
from flask_cors import CORS

from game_json import heroes, classes, races

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/heroes', methods=['GET'])
def get_heroes():
    return jsonify(heroes)


@app.route('/classes', methods=['GET'])
def get_classes():
    return jsonify(classes)


@app.route('/races', methods=['GET'])
def get_races():
    return jsonify(races)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
