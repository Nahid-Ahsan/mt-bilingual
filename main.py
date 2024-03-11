from flask import Flask, request, jsonify
from bangla import *

app = Flask(__name__)


@app.route('/response', methods=['POST'])
def queryresonse():
    try:
        query = request.json.get('query', '')
        # print(query)  
        result = translate(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
	app.run(debug=True)
	gunicorn -w 4 -b 0.0.0.0:5000 main:app


