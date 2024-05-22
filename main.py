from flask import Flask, request, jsonify
from bangla import *
from english import *
import gunicorn
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/bangla', methods=['POST'])
@cross_origin()
def queryresonse_bn():
    try:
        query = request.json.get('query', '')
        # print(query)  
        result = translate_bn(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/english', methods=['POST'])
def queryresonse_en():
    try:
        query = request.json.get('query', '')
        # print(query)  
        result = translate_en(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
	    
if __name__ == "__main__":
	app.run(debug=True, port = 5000, host = "0.0.0.0" )
	
	# gunicorn -w 4 -b 0.0.0.0:5000 main:app


	# gunicorn -w 4 -b 0.0.0.0:5000 main:app
