from flask import Flask, request, jsonify
from bangla import *
from english import *
import gunicorn
app = Flask(__name__)


@app.route('/bangla', methods=['POST'])
def queryresonse():
    try:
        query = request.json.get('query', '')
        # print(query)  
        result = translate_bn(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/english', methods=['POST'])
def queryresonse():
    try:
        query = request.json.get('query', '')
        # print(query)  
        result = translate_en(query)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
	    
if __name__ == "__main__":
	gunicorn -w 4 -b 0.0.0.0:5000 main:app
	app.run(debug=True)
	


