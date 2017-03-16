from flask import Flask,jsonify,request
from pymongo import MongoClient


import sys,os,json
import pandas as pd

app = Flask(__name__)
db = MongoClient()
olam = db['olam']['olam-enml']
APP_ROOT = os.path.dirname(__file__)
def import_csv_to_db():
	file_res = os.path.join(APP_ROOT, 'olam-enml.csv')
	print file_res
	csv_data = pd.read_csv(file_res,sep='\t')
	json_data = json.loads(csv_data.to_json(orient='records'))
	olam.remove()
	olam.insert(json_data)

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
	import_csv_to_db()
	app.run(debug=True, threaded=False, host='127.0.0.1',port=1122)