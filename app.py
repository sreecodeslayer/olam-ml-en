from flask import Flask,jsonify,request
from pymongo import MongoClient

app = Flask(__name__)
db = MongoClient()
olam = db['olam']['olam-enml']

@app.route('/')
def index():
	return jsonify({'hi':'welcome!'})

@app.route('/search',methods=['GET'])
def search():
	result = []
	text = request.args['text']
	r = olam.find({'malayalam_definition':text})
	for i in r:
		result.append(i['english_word'])

	return jsonify({'result':result})

if __name__ == '__main__':
	app.run(debug=True, threaded=False, host='127.0.0.1',port=1122)